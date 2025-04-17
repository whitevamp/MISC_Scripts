import os
import shutil
import random
import string
import json
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def generate_random_digits(length=3):
    return ''.join(random.choices(string.digits, k=length))


def choose_directory(title="Choose folder"):
    return filedialog.askdirectory(title=title)


def choose_file(title="Choose template JSON file"):
    return filedialog.askopenfilename(title=title, filetypes=[("JSON files", "*.json")])


def get_mesh_size(width, height):
    def round_mesh(x):
        return int(round(x))

    mesh_base = 4  # Can be made user-configurable later

    ratio = width / height
    if ratio >= 1:
        x = round_mesh(mesh_base * ratio)
        z = mesh_base
    else:
        x = mesh_base
        z = round_mesh(mesh_base / ratio)

    return x, z


def safe_texture_resize(img, min_size=512):
    width, height = img.size
    safe_width = max(min_size, ((width + 3) // 4) * 4)
    safe_height = max(min_size, ((height + 3) // 4) * 4)

    if (width, height) != (safe_width, safe_height):
        print(f"[RESIZE] Resizing from {width}x{height} → {safe_width}x{safe_height}")
        new_img = Image.new("RGBA", (safe_width, safe_height), (0, 0, 0, 0))
        new_img.paste(img, ((safe_width - width) // 2, (safe_height - height) // 2))
        return new_img, safe_width, safe_height
    return img, width, height


def process_images(src_folder, dest_folder, template_path, prefix):
    print(f"[INFO] Starting processing:\n  Source: {src_folder}\n  Destination: {dest_folder}\n  Template: {template_path}\n  Prefix: {prefix}")
    for root, _, files in os.walk(src_folder):
        for file in files:
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext not in ['.png', '.jpg', '.jpeg']:
                continue

            try:
                file_path = os.path.join(root, file)
                print(f"[INFO] Processing file: {file_path}")
                img = Image.open(file_path)

                # Convert and clean
                img = img.convert("RGBA")
                img, width, height = safe_texture_resize(img)

                # Build folder and names
                random_suffix = generate_random_digits()
                folder_name = f"{prefix}{random_suffix}"
                output_folder = os.path.join(dest_folder, folder_name)
                os.makedirs(output_folder, exist_ok=True)

                new_image_path = os.path.join(output_folder, "_BaseColorMap.png")
                img.save(new_image_path, format="PNG")
                print(f"[OK] Saved image: {new_image_path}")

                # Load and modify template
                with open(template_path, 'r') as f:
                    template = json.load(f)

                mesh_x, mesh_z = get_mesh_size(width, height)
                template["Vector"]["colossal_MeshSize"]["x"] = mesh_x
                template["Vector"]["colossal_MeshSize"]["z"] = mesh_z

                decal_path = os.path.join(output_folder, "decal.json")
                with open(decal_path, 'w') as f:
                    json.dump(template, f, indent=4)

                print(f"[OK] Saved decal JSON: {decal_path}")

            except Exception as e:
                print(f"[ERROR] Failed to process {file}: {e}")


def main():
    root = tk.Tk()
    root.withdraw()  # Hide main window

    src_folder = choose_directory("Select Source Folder")
    if not src_folder:
        return

    dest_folder = choose_directory("Select Destination Folder")
    if not dest_folder:
        return

    template_path = choose_file("Select Template JSON File")
    if not template_path:
        return

    prefix_input = tk.simpledialog.askstring("Input", "Enter folder prefix name (e.g., 'tree'):")
    if not prefix_input:
        return

    process_images(src_folder, dest_folder, template_path, prefix_input)
    messagebox.showinfo("Complete", "Image processing completed!")


if __name__ == "__main__":
    main()
