import re
import os
import shutil
from tkinter import Tk, filedialog, Checkbutton, IntVar, Label, Button
from PIL import Image, UnidentifiedImageError
from tkinter.messagebox import showerror

# Define keyword lists based on priority levels
high_priority_keywords = [
    r"mudrock", r"wakamo", r"skadi", r"surtr", r"kirara", r"mika", r"eula", 
    r"mona", r"raiden_shogun", r"kafka", r"himeko", r"stelle", r"bailu", r"firefly", 
    r"kamisato_clan", r"black_prince_XL_pony_v1", r"queen elizabeth", r"sushang", 
    r"texas_", r"astesia", r"terakomari", r"sephie michaela deviluke", r"clara", 
    r"ReineBase", r"PavoliaReine", r"yae miko", r"raiden shogun", "CHAR-BBFatePonyXL", r"phkimo", r"NakiriAyamePDXL", r"achilles_"
]

medium_priority_keywords = [
    # Add medium-priority keywords here when needed
]

low_priority_keywords = [
    r"2 girls", r"2girls", r"The other beauty", r"1 girl"
]

def extract_keywords(metadata):
    """
    Extracts all matching keywords from metadata, starting with high-priority,
    then medium-priority, and finally low-priority if necessary.
    Returns a list of matched keywords.
    """
    if not metadata:
        return []

    matched_keywords = []

    # Check for matches in high-priority keywords
    for keyword in high_priority_keywords:
        if re.search(rf"(?:<lora:\s*{keyword}|{keyword})", metadata, re.IGNORECASE):
            matched_keywords.append(keyword)

    # Check for matches in medium-priority keywords if no high-priority matches found
    if not matched_keywords:
        for keyword in medium_priority_keywords:
            if re.search(rf"(?:<lora:\s*{keyword}|{keyword})", metadata, re.IGNORECASE):
                matched_keywords.append(keyword)

    # Check for matches in low-priority keywords if no higher-priority matches found
    if not matched_keywords:
        for keyword in low_priority_keywords:
            if re.search(rf"(?:<lora:\s*{keyword}|{keyword})", metadata, re.IGNORECASE):
                matched_keywords.append(keyword)

    return matched_keywords  # Return all matches found

def sanitize_folder_name(name):
    return re.sub(r'[<>:"/\\|?*]', "_", name)

def get_metadata(image_path):
    try:
        image = Image.open(image_path)
        metadata = image.info.get("parameters", "")
        print(f"Metadata for {image_path}: {metadata}")
        return metadata
    except UnidentifiedImageError:
        print(f"Warning: Could not identify image format for {image_path}")
        return None
        
# Fallback extraction for <lora:...> format if no keywords are matched
def extract_lora_name(metadata):
    """
    Extracts the first <lora:...> name found in metadata, used as a fallback if no keywords are matched.
    """
    if not metadata:
        return None
    
    lora_name = None
    # Updated regex to capture common formats for Lora tags
    match = re.search(r'(?:Lora hashes:\s*"|lora:|<lora:)([a-zA-Z0-9_-]+)', metadata)
    if match:
        lora_name = match.group(1)  # Extract the identifier

    if lora_name:
        lora_name = re.sub(r'[<>:"/\\|?*]', '_', lora_name)
    
    return lora_name

def rename_and_move_files(input_dir, output_dir, move_files):
    unnamed_folder = os.path.join(output_dir, "UnNamed_Images")
    os.makedirs(unnamed_folder, exist_ok=True)

    for root, _, files in os.walk(input_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            if not file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue

            metadata = get_metadata(file_path)
            matched_keywords = extract_keywords(metadata)

            if not matched_keywords:
                # Fallback to extract_lora_name if no keywords matched
                lora_name = extract_lora_name(metadata)
                if lora_name:
                    matched_keywords = [lora_name]

            if matched_keywords:
                # Combine matched keywords or fallback name into a single folder and base name
                combined_name = "&".join(matched_keywords).replace(" ", "").lower()
                dest_folder = os.path.join(output_dir, sanitize_folder_name(combined_name))
                os.makedirs(dest_folder, exist_ok=True)

                base_name, extension = os.path.splitext(filename)
                new_filename = f"{combined_name}{extension}"
                
                # Handle naming conflicts by adding a counter
                counter = 1
                while os.path.exists(os.path.join(dest_folder, new_filename)):
                    new_filename = f"{combined_name}({counter}){extension}"
                    counter += 1

                dest_path = os.path.join(dest_folder, new_filename)
                print(f"Moving {file_path} to {dest_path}")
                if move_files:
                    shutil.move(file_path, dest_path)
                else:
                    shutil.copy(file_path, dest_path)
            else:
                # If no keywords or fallback name found, move to UnNamed_Images folder
                dest_path = os.path.join(unnamed_folder, filename)
                print(f"No match found. Moving {file_path} to {dest_path}")
                if move_files:
                    shutil.move(file_path, dest_path)
                else:
                    shutil.copy(file_path, dest_path)

def select_directory(title):
    return filedialog.askdirectory(title=title)

def start_processing():
    input_dir = select_directory("Select Input Directory")
    output_dir = select_directory("Select Output Directory")

    if not input_dir or not output_dir:
        showerror("Error", "Please select both input and output directories.")
        return

    rename_and_move_files(input_dir, output_dir, move_files.get())

def create_ui():
    root = Tk()
    root.title("Image Metadata Organizer")

    Label(root, text="Organize images by keywords in metadata").pack(pady=10)
    global move_files
    move_files = IntVar()
    Checkbutton(root, text="Move files (leave unchecked to copy)", variable=move_files).pack()

    Button(root, text="Select Directories and Start", command=start_processing).pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    create_ui()
