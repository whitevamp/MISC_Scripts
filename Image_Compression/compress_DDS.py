# pip install pillow pillow-dds
import os
from PIL import Image

# Check if Resampling is available (Pillow 10 and newer)
try:
    from PIL import Resampling
    LANCZOS = Resampling.LANCZOS
except ImportError:
    # Fallback for older Pillow versions
    LANCZOS = Image.LANCZOS

# Directory where the script is run from
base_directory = os.getcwd()

# Function to compress DDS files and create mipmaps
def compress_and_mipmap(file_path, overwrite):
    try:
        # Open DDS texture
        with Image.open(file_path) as img:
            print(f"Processing: {file_path}")

            # Ensure the file is a DDS texture
            if img.format != 'DDS':
                print(f"Skipping non-DDS file: {file_path}")
                return

            # Create mipmaps by generating resized versions of the image
            mipmaps = [img]
            width, height = img.size
            while width > 1 and height > 1:
                width //= 2
                height //= 2
                # Use the correct LANCZOS resampling depending on Pillow version
                mipmaps.append(img.resize((width, height), LANCZOS))

            if overwrite:
                # Overwrite the original file
                mipmaps[0].save(file_path, format="DDS", mipmap_levels=len(mipmaps))
                print(f"Overwritten: {file_path}")
            else:
                # Save with "_mip" suffix
                mipmap_file_path = file_path.replace(".dds", "_mip.dds")
                mipmaps[0].save(mipmap_file_path, format="DDS", mipmap_levels=len(mipmaps))
                print(f"Saved with mipmaps: {mipmap_file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Function to recursively go through directories and process DDS files
def process_directory(directory, overwrite):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".dds"):
                file_path = os.path.join(root, file)
                compress_and_mipmap(file_path, overwrite)

# Prompt the user to choose whether to overwrite or rename files
def ask_overwrite_option():
    while True:
        choice = input("Do you want to overwrite the original DDS files? (y/n): ").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

# Main process
if __name__ == "__main__":
    # Ensure user is asked about overwriting files before any processing starts
    overwrite_files = ask_overwrite_option()

    # Start processing DDS files based on user input
    process_directory(base_directory, overwrite_files)


