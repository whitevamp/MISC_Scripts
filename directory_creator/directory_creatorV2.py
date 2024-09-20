import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def create_directories():
    try:
        # Get the number of directories and path
        num_dirs = int(num_dirs_var.get())
        base_path = path_var.get()
        depth1 = int(depth_var1.get())
        depth2 = int(depth_var2.get()) if extra_dirs_var.get() else 0

        if not base_path:
            raise ValueError("Please select a base path.")

        # Get directory names from the input fields for both primary and secondary sections
        dir_names1 = [dir_name_var1[i].get() for i in range(depth1)]
        dir_names2 = [dir_name_var2[i].get() for i in range(depth2)] if depth2 > 0 else []

        # Create directories for both primary and secondary sections
        for i in range(1, num_dirs + 1):
            top_dir = dir_names1[0].replace("{n}", str(i))
            full_path1 = os.path.join(base_path, top_dir, *dir_names1[1:])
            os.makedirs(full_path1, exist_ok=True)

            if depth2 > 0:
                full_path2 = os.path.join(base_path, top_dir, *dir_names2)
                os.makedirs(full_path2, exist_ok=True)

        messagebox.showinfo("Success", f"Successfully created {num_dirs} directories!")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        path_var.set(directory)

def update_depth_fields1(*args):
    # Clear existing text fields for the primary section
    for widget in dir_frame1.winfo_children():
        widget.destroy()

    try:
        depth1 = int(depth_var1.get())
    except ValueError:
        depth1 = 1

    # Create the input fields for the primary directory names
    for i in range(depth1):
        label = tk.Label(dir_frame1, text=f"Primary directory level {i+1}:")
        label.grid(row=i, column=0, padx=5, pady=5)
        entry = tk.Entry(dir_frame1, textvariable=dir_name_var1[i])
        entry.grid(row=i, column=1, padx=5, pady=5)

def update_depth_fields2(*args):
    # Clear existing text fields for the secondary section
    for widget in dir_frame2.winfo_children():
        widget.destroy()

    try:
        depth2 = int(depth_var2.get())
    except ValueError:
        depth2 = 1

    # Create the input fields for the secondary directory names
    for i in range(depth2):
        label = tk.Label(dir_frame2, text=f"Secondary directory level {i+1}:")
        label.grid(row=i, column=0, padx=5, pady=5)
        entry = tk.Entry(dir_frame2, textvariable=dir_name_var2[i])
        entry.grid(row=i, column=1, padx=5, pady=5)

def toggle_extra_directories():
    if extra_dirs_var.get():
        extra_frame.grid(row=3, column=0, sticky="ew")
        update_depth_fields2()
    else:
        extra_frame.grid_forget()

# Setup the UI
root = tk.Tk()
root.title("Directory Structure Creator")

# Variables
num_dirs_var = tk.StringVar(value="1")
path_var = tk.StringVar()
depth_var1 = tk.StringVar(value="1")
depth_var2 = tk.StringVar(value="1")
dir_name_var1 = [tk.StringVar(value=f"Replacer {n}") for n in range(20)]
dir_name_var2 = [tk.StringVar(value=f"Secondary {n}") for n in range(20)]
extra_dirs_var = tk.BooleanVar(value=False)

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

# Primary directory depth dropdown
ttk.Label(frame, text="Primary directory depth:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
depth_menu1 = ttk.OptionMenu(frame, depth_var1, "1", *[str(i) for i in range(1, 21)], command=update_depth_fields1)
depth_menu1.grid(row=2, column=1, padx=5, pady=5)

# Directory names frame (dynamic)
dir_frame1 = ttk.Frame(root, padding="10")
dir_frame1.grid(row=1, column=0, sticky="ew")
update_depth_fields1()

# Checkbox for extra directories
ttk.Checkbutton(frame, text="Include secondary directory structure", variable=extra_dirs_var, command=toggle_extra_directories).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Extra directories frame (initially hidden)
extra_frame = ttk.Frame(root, padding="10")
extra_frame.grid_forget()

# Secondary directory depth dropdown
ttk.Label(extra_frame, text="Secondary directory depth:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
depth_menu2 = ttk.OptionMenu(extra_frame, depth_var2, "1", *[str(i) for i in range(1, 21)], command=update_depth_fields2)
depth_menu2.grid(row=0, column=1, padx=5, pady=5)

# Secondary directory names frame (dynamic)
dir_frame2 = ttk.Frame(extra_frame, padding="10")
dir_frame2.grid(row=1, column=0, sticky="ew")

# Create directories button
ttk.Button(root, text="Create Directories", command=create_directories).grid(row=4, column=0, padx=10, pady=10)

root.mainloop()
