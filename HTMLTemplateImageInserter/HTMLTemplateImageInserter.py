import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import urllib.parse

# Function to scan directory for images and return both encoded and unencoded paths
def scan_directory(directory):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    images = []
    encoded_images = []
    
    for f in Path(directory).rglob("*"):
        if f.suffix.lower() in image_extensions:
            # Use absolute path for the file
            unencoded_path = os.path.normpath(str(f.resolve()))  # Ensure consistent absolute path
            relative_path = str(f.relative_to(directory)).replace("\\", "/")
            encoded_path = urllib.parse.quote(relative_path)  # Use encoded relative path for HTML
            
            images.append(unencoded_path)
            encoded_images.append(encoded_path)

    return images, encoded_images

# Function to handle copying or moving images and return paths for the template
def handle_images(images, input_folder, output_folder, action, preserve_structure):
    processed_images = []
    for img in images:
        source_path = Path(img)
        
        if preserve_structure:
            # Get the relative path
            relative_path = source_path.relative_to(input_folder)
            destination_path = Path(output_folder) / relative_path
        else:
            # Flatten the structure and only use the filename
            destination_path = Path(output_folder) / source_path.name

        # Ensure the destination directory exists
        destination_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            if action == "Copy":
                if source_path != destination_path:  # Check to avoid copying to itself
                    shutil.copy2(source_path, destination_path)
            elif action == "Move":
                if source_path != destination_path:  # Check to avoid moving to itself
                    shutil.move(source_path, destination_path)
            processed_images.append(str(destination_path))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to {action.lower()} image '{img}': {e}")

    return processed_images

# Function to update the HTML template
def update_template(template_path, images, output_directory, timeout, preserve_structure):
    # Convert images to encoded paths for HTML
    encoded_images = [urllib.parse.quote(str(Path(image).relative_to(output_directory))) for image in images]

    # Read the HTML template file
    try:
        with open(template_path, 'r', encoding='utf-8') as file:
            template_content = file.read()
        
        # Generate the paths list for the HTML file
        html_image_paths = ',\n    '.join(f'"{img}"' for img in encoded_images)
        
        # Replace placeholder text in the template with the image paths
        updated_html = template_content.replace('// Add your image filenames here', html_image_paths)
        
        # Update the timeout in the template
        updated_html = updated_html.replace('setTimeout(loadNextImages, 10000);', f'setTimeout(loadNextImages, {timeout});')
        
        # Save the modified template to the output directory
        output_template_path = Path(output_directory) / "updated_template.html"
        with open(output_template_path, 'w', encoding='utf-8') as file:
            file.write(updated_html)
        
        print(f"Template updated successfully and saved at: {output_template_path}")
        
    except Exception as e:
        print(f"Failed to update the template: {e}")

# Function to start processing
def process():
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()
    template_file = template_file_var.get()
    timeout = timeout_var.get()
    action = action_var.get()
    preserve_structure = preserve_structure_var.get()  # Get the checkbox state

    if not (input_folder and output_folder and template_file):
        messagebox.showwarning("Input Required", "Please specify all input and output paths.")
        return

    if not os.path.isdir(input_folder):
        messagebox.showerror("Error", "Invalid input folder.")
        return

    if not os.path.isfile(template_file):
        messagebox.showerror("Error", "Invalid template file.")
        return

    # Unpack images and encoded_images separately
    images, _ = scan_directory(input_folder)
    
    if not images:
        messagebox.showwarning("No Images Found", "No image files found in the selected folder.")
        return

    # Handle copying or moving images if specified and get the processed paths
    if action in ["Copy", "Move"]:
        processed_images = handle_images(images, input_folder, output_folder, action, preserve_structure)
    else:
        processed_images = images

    # Update the HTML template with the paths and timeout
    update_template(template_file, processed_images, output_folder, timeout, preserve_structure)

# GUI Setup
root = tk.Tk()
root.title("HTML Template Image Inserter")
root.geometry("500x350")

# Variables
input_folder_var = tk.StringVar()
output_folder_var = tk.StringVar()
template_file_var = tk.StringVar()
timeout_var = tk.IntVar(value=10000)
action_var = tk.StringVar(value="Do Nothing")
preserve_structure_var = tk.BooleanVar(value=True)  # Add preserve structure checkbox

# UI Elements
tk.Label(root, text="Select Input Folder:").pack(pady=5)
tk.Entry(root, textvariable=input_folder_var, width=60).pack(pady=5)
tk.Button(root, text="Browse", command=lambda: input_folder_var.set(filedialog.askdirectory())).pack()

tk.Label(root, text="Select Output Folder:").pack(pady=5)
tk.Entry(root, textvariable=output_folder_var, width=60).pack(pady=5)
tk.Button(root, text="Browse", command=lambda: output_folder_var.set(filedialog.askdirectory())).pack()

tk.Label(root, text="Select HTML Template File:").pack(pady=5)
tk.Entry(root, textvariable=template_file_var, width=60).pack(pady=5)
tk.Button(root, text="Browse", command=lambda: template_file_var.set(filedialog.askopenfilename(filetypes=[("HTML files", "*.html")]))).pack()

tk.Label(root, text="Set Wallpaper Timeout (ms):").pack(pady=5)
tk.Entry(root, textvariable=timeout_var).pack(pady=5)

# Action selection for Copy/Move/Do Nothing
tk.Label(root, text="Action for Images Found:").pack(pady=5)
tk.OptionMenu(root, action_var, "Do Nothing", "Copy", "Move").pack()

# Preserve file structure checkbox
tk.Checkbutton(root, text="Preserve File Structure", variable=preserve_structure_var).pack(pady=10)

tk.Button(root, text="Process", command=process).pack(pady=20)

# Run the GUI
root.mainloop()
