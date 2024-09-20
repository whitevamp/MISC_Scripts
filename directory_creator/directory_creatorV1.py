import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def create_directories():
    try:
        # Get the number of directories and path
        num_dirs = int(num_dirs_var.get())
        base_path = path_var.get()
        depth = int(depth_var.get())

        if not base_path:
            raise ValueError("Please select a base path.")

        # Get directory names from the input fields
        dir_names = [dir_name_var[i].get() for i in range(depth)]

        # Create directories
        for i in range(1, num_dirs + 1):
            top_dir = dir_names[0].replace("{n}", str(i))
            full_path = os.path.join(base_path, top_dir, *dir_names[1:])
            os.makedirs(full_path, exist_ok=True)

        messagebox.showinfo("Success", f"Successfully created {num_dirs} directories!")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        path_var.set(directory)

def update_depth_fields(*args):
    # Clear existing text fields
    for widget in dir_frame.winfo_children():
        widget.destroy()

    try:
        depth = int(depth_var.get())
    except ValueError:
        depth = 1

    # Create the input fields for directory names
    for i in range(depth):
        label = tk.Label(dir_frame, text=f"Name of directory level {i+1}:")
        label.grid(row=i, column=0, padx=5, pady=5)
        entry = tk.Entry(dir_frame, textvariable=dir_name_var[i])
        entry.grid(row=i, column=1, padx=5, pady=5)

# Setup the UI
root = tk.Tk()
root.title("Directory Structure Creator")

# Variables
num_dirs_var = tk.StringVar(value="1")
path_var = tk.StringVar()
depth_var = tk.StringVar(value="1")
dir_name_var = [tk.StringVar(value=f"Replacer {n}") for n in range(20)]

# Main frame
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="ew")

# Number of directories input
ttk.Label(frame, text="Number of directories:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
ttk.Entry(frame, textvariable=num_dirs_var).grid(row=0, column=1, padx=5, pady=5)

# Base path input
ttk.Label(frame, text="Base path:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
ttk.Entry(frame, textvariable=path_var).grid(row=1, column=1, padx=5, pady=5)
ttk.Button(frame, text="Browse", command=select_directory).grid(row=1, column=2, padx=5, pady=5)

# Directory depth dropdown
ttk.Label(frame, text="Depth of directories:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
depth_menu = ttk.OptionMenu(frame, depth_var, "1", *[str(i) for i in range(1, 21)], command=update_depth_fields)
depth_menu.grid(row=2, column=1, padx=5, pady=5)

# Directory names frame (dynamic)
dir_frame = ttk.Frame(root, padding="10")
dir_frame.grid(row=1, column=0, sticky="ew")
update_depth_fields()

# Create directories button
ttk.Button(root, text="Create Directories", command=create_directories).grid(row=2, column=0, padx=10, pady=10)

root.mainloop()
