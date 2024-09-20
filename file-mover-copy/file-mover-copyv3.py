import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def move_or_copy_files():
    try:
        # Get source and destination paths for multiple files
        source_path = source_var.get()
        dest_path = dest_var.get()
        num_files = len(os.listdir(source_path)) if detect_files_var.get() else int(num_files_var.get())
        tld_path = tld_var.get().strip()
        target_subfolder = subfolder_var.get().strip()

        if not source_path or not dest_path:
            raise ValueError("Please select both source and destination folders.")
        
        if not target_subfolder:
            raise ValueError("Please specify the subfolder path for placing the files (e.g., textures/interface/objects).")

        # Get subdirectories in the destination path for multiple files
        sub_dirs = [os.path.join(dest_path, f"{tld_path} {i+1}", target_subfolder) for i in range(num_files)]

        # Check if subdirectories exist
        for sub_dir in sub_dirs:
            if not os.path.exists(sub_dir):
                raise ValueError(f"Subdirectory does not exist: {sub_dir}")

        # Get all files in the source directory
        files = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))][:num_files]
        
        if not files:
            raise ValueError("No files found in the source directory.")

        # Perform the move or copy operation for multiple files
        for i, file_name in enumerate(files):
            src_file = os.path.join(source_path, file_name)
            dest_file = os.path.join(sub_dirs[i], file_name)
            
            if move_files_var.get():
                shutil.move(src_file, dest_file)
            else:
                shutil.copy(src_file, dest_file)

        # Handle copying of the single file if checkbox is selected
        if copy_single_file_var.get():
            single_source_file = single_file_var.get().strip()
            single_target_subfolder = single_subfolder_var.get().strip()

            if not single_source_file or not single_target_subfolder:
                raise ValueError("Please specify both the source file and destination subfolder for the single file.")

            # Get subdirectories for single file copy
            single_sub_dirs = [os.path.join(dest_path, f"{tld_path} {i+1}", single_target_subfolder) for i in range(num_files)]
            
            # Check if subdirectories exist for single file copy
            for single_sub_dir in single_sub_dirs:
                if not os.path.exists(single_sub_dir):
                    raise ValueError(f"Subdirectory does not exist: {single_sub_dir}")

            # Copy or move the single file to all specified subdirectories
            for i in range(num_files):
                dest_file = os.path.join(single_sub_dirs[i], os.path.basename(single_source_file))
                if move_files_var.get():
                    shutil.move(single_source_file, dest_file)
                else:
                    shutil.copy(single_source_file, dest_file)

        messagebox.showinfo("Success", f"Successfully {'moved' if move_files_var.get() else 'copied'} files!")
    
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def select_source_folder():
    folder = filedialog.askdirectory()
    if folder:
        source_var.set(folder)
        if detect_files_var.get():
            num_files_var.set(len([f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]))

def select_dest_folder():
    folder = filedialog.askdirectory()
    if folder:
        dest_var.set(folder)

def select_single_file():
    file = filedialog.askopenfilename()
    if file:
        single_file_var.set(file)

def toggle_file_count(*args):
    if detect_files_var.get():
        num_files_entry.config(state='disabled')
        if source_var.get():
            num_files_var.set(len([f for f in os.listdir(source_var.get()) if os.path.isfile(os.path.join(source_var.get(), f))]))
    else:
        num_files_entry.config(state='normal')

def toggle_single_file_section():
    if copy_single_file_var.get():
        single_file_frame.grid(row=8, column=0, columnspan=3, padx=10, pady=10)
    else:
        single_file_frame.grid_remove()

# Setup the UI
root = tk.Tk()
root.title("Move/Copy Files to Subdirectories")

# Variables
source_var = tk.StringVar()
dest_var = tk.StringVar()
num_files_var = tk.StringVar(value="0")
move_files_var = tk.BooleanVar(value=False)
detect_files_var = tk.BooleanVar(value=True)
copy_single_file_var = tk.BooleanVar(value=False)
single_file_var = tk.StringVar()
tld_var = tk.StringVar(value="Replacer")
subfolder_var = tk.StringVar(value="textures/interface/objects")
single_subfolder_var = tk.StringVar(value="meshes/interface/logo")

# Source Folder Selection
tk.Label(root, text="Source Folder:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
tk.Entry(root, textvariable=source_var, width=40).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_source_folder).grid(row=0, column=2, padx=10, pady=10)

# Destination Folder Selection
tk.Label(root, text="Destination Folder:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
tk.Entry(root, textvariable=dest_var, width=40).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_dest_folder).grid(row=1, column=2, padx=10, pady=10)

# TLD and Subfolder Name
tk.Label(root, text="Top-Level Directory (TLD) Name:").grid(row=2, column=0, padx=10, pady=10, sticky='w')
tk.Entry(root, textvariable=tld_var, width=40).grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Subfolder Path:").grid(row=3, column=0, padx=10, pady=10, sticky='w')
tk.Entry(root, textvariable=subfolder_var, width=40).grid(row=3, column=1, padx=10, pady=10)

# File Count and Detection
tk.Checkbutton(root, text="Auto-detect number of files", variable=detect_files_var, command=toggle_file_count).grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='w')
tk.Label(root, text="Number of files:").grid(row=5, column=0, padx=10, pady=10, sticky='w')
num_files_entry = tk.Entry(root, textvariable=num_files_var, width=40)
num_files_entry.grid(row=5, column=1, padx=10, pady=10)

# Move/Copy Option
tk.Checkbutton(root, text="Move files instead of copy", variable=move_files_var).grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='w')

# Single File Copy Section
tk.Checkbutton(root, text="Also copy a single file to all subdirectories", variable=copy_single_file_var, command=toggle_single_file_section).grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky='w')

# Frame for Single File Section
single_file_frame = tk.Frame(root)
tk.Label(single_file_frame, text="Single File:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
tk.Entry(single_file_frame, textvariable=single_file_var, width=40).grid(row=0, column=1, padx=10, pady=10)
tk.Button(single_file_frame, text="Browse", command=select_single_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(single_file_frame, text="Destination Subfolder for Single File:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
tk.Entry(single_file_frame, textvariable=single_subfolder_var, width=40).grid(row=1, column=1, padx=10, pady=10)

# Initial state of single file frame
single_file_frame.grid_remove()

# Start Button
tk.Button(root, text="Start", command=move_or_copy_files).grid(row=9, column=1, padx=10, pady=20)

root.mainloop()
