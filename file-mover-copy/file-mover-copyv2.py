import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def move_or_copy_files():
    try:
        # Get source and destination paths
        source_path = source_var.get()
        dest_path = dest_var.get()
        num_files = len(os.listdir(source_path)) if detect_files_var.get() else int(num_files_var.get())
        tld_path = tld_var.get().strip()
        target_subfolder = subfolder_var.get().strip()

        if not source_path or not dest_path:
            raise ValueError("Please select both source and destination folders.")
        
        if not target_subfolder:
            raise ValueError("Please specify the subfolder path for placing the files (e.g., textures/interface/objects).")

        # Get subdirectories in the destination path
        sub_dirs = [os.path.join(dest_path, f"{tld_path} {i+1}", target_subfolder) for i in range(num_files)]

        # Check if subdirectories exist
        for sub_dir in sub_dirs:
            if not os.path.exists(sub_dir):
                raise ValueError(f"Subdirectory does not exist: {sub_dir}")

        # Get all files in the source directory
        files = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))][:num_files]
        
        if not files:
            raise ValueError("No files found in the source directory.")

        # Perform the move or copy operation
        for i, file_name in enumerate(files):
            src_file = os.path.join(source_path, file_name)
            dest_file = os.path.join(sub_dirs[i], file_name)
            
            if move_files_var.get():
                shutil.move(src_file, dest_file)
            else:
                shutil.copy(src_file, dest_file)
        
        messagebox.showinfo("Success", f"Successfully {'moved' if move_files_var.get() else 'copied'} {num_files} files!")
    
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

def toggle_file_count(*args):
    if detect_files_var.get():
        num_files_entry.config(state='disabled')
        if source_var.get():
            num_files_var.set(len([f for f in os.listdir(source_var.get()) if os.path.isfile(os.path.join(source_var.get(), f))]))
    else:
        num_files_entry.config(state='normal')

# Setup the UI
root = tk.Tk()
root.title("Move/Copy Files to Subdirectories")

# Variables
source_var = tk.StringVar()
dest_var = tk.StringVar()
num_files_var = tk.StringVar(value="0")
move_files_var = tk.BooleanVar(value=False)
detect_files_var = tk.BooleanVar(value=True)
tld_var = tk.StringVar(value="Replacer")
subfolder_var = tk.StringVar(value="textures/interface/objects")

# Main frame
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="ew")

# Source folder input
ttk.Label(frame, text="Source folder:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
ttk.Entry(frame, textvariable=source_var).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame, text="Browse", command=select_source_folder).grid(row=0, column=2, padx=5, pady=5)

# Destination folder input
ttk.Label(frame, text="Destination folder:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
ttk.Entry(frame, textvariable=dest_var).grid(row=1, column=1, padx=5, pady=5)
ttk.Button(frame, text="Browse", command=select_dest_folder).grid(row=1, column=2, padx=5, pady=5)

# Top-level directory (TLD) input
ttk.Label(frame, text="Top-level directory (e.g., Replacer):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
ttk.Entry(frame, textvariable=tld_var).grid(row=2, column=1, padx=5, pady=5)

# Subfolder path input
ttk.Label(frame, text="Place files in subfolder (e.g., textures/interface/objects):").grid(row=3, column=0, sticky="w", padx=5, pady=5)
ttk.Entry(frame, textvariable=subfolder_var).grid(row=3, column=1, padx=5, pady=5)

# Number of files input
ttk.Checkbutton(frame, text="Auto-detect number of files", variable=detect_files_var, command=toggle_file_count).grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="w")
ttk.Label(frame, text="Number of files:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
num_files_entry = ttk.Entry(frame, textvariable=num_files_var)
num_files_entry.grid(row=5, column=1, padx=5, pady=5)
toggle_file_count()  # Set initial state based on detect_files_var

# Move or Copy option
ttk.Checkbutton(frame, text="Move files instead of copying", variable=move_files_var).grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Action button
ttk.Button(root, text="Move/Copy Files", command=move_or_copy_files).grid(row=7, column=0, padx=10, pady=10, columnspan=3)

root.mainloop()
