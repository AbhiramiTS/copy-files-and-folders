import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from copy_files import copy_files, copy_dirs
from log_config import get_latest_log_file

# Create main window
root = tk.Tk()
root.title("Directory Copier")
root.geometry("800x500")
root.config(bg="#ffffff")  # Updated to a cleaner white background

# Function to browse directory
def browse_directory(entry_field):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, folder_selected)

# Add status label at the bottom
status_label = tk.Label(root, text="", font=("Segoe UI", 12), bg="#ffffff")
status_label.grid(row=6, column=0, columnspan=3, pady=10)

# Function to update status with color
def update_status(message, color):
    status_label.config(text=message, fg=color)

# Function to download the log file
def download_log_file():
    import shutil
    log_file_path = get_latest_log_file()
    if log_file_path is None:
        messagebox.showerror("Error", "No log file available to download.")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if save_path:
        shutil.copy(log_file_path, save_path)
        messagebox.showinfo("Download", "Log file downloaded successfully.")

# Function to update the visibility of the log file link
def update_log_file_link():
    log_file_path = get_latest_log_file()
    if log_file_path is None:
        log_file_link.grid_remove()  # Hide the log file link
    else:
        log_file_link.grid()  # Show the log file link

# Add log file link (initially hidden)
log_file_link = tk.Label(root, text="View Log File", font=("Segoe UI", 12, "underline"), fg="blue", bg="#ffffff", cursor="hand2")
log_file_link.grid(row=7, column=0, columnspan=3, pady=10)
log_file_link.bind("<Button-1>", lambda e: download_log_file())
log_file_link.grid_remove()  # Initially hide the link



# Update the start_copy function
def start_copy():
    source_dir = source_entry.get().strip()
    dest_dir = dest_entry.get().strip()

    if not source_dir or not dest_dir:
        update_status("Error: Please enter both source and destination directories.", "red")
        return

    copy_type = copy_type_var.get().lower()

    if copy_type == 'files':
        extensions_input = extensions_entry.get().strip()
        if not extensions_input:
            update_status("Error: Please enter file extensions.", "red")
            return
        extensions = tuple(set("." + ext for ext in extensions_input.split(',')))
        print(f"Copying files with extensions: {extensions}")
        return_val = copy_files(source_dir, dest_dir, extensions)
    else:
        compress = compress_var.get()
        if compress:
            print("Compressing and copying the entire directory...")
        else:
            print("Copying the entire directory without compression...")
        return_val = copy_dirs(source_dir, dest_dir, compress)
    
    if return_val:
        update_status("Success: Operation completed successfully.", "green")
    else:
        update_status("Error: Operation failed. Please check the log file.", "red")
        update_log_file_link()
    
 
    # For now, just printing out the input values for demonstration
    print(f"Source Directory: {source_dir}")
    print(f"Destination Directory: {dest_dir}")
    print(f"Copy Type: {copy_type}")
    # Call update_log_file_link after performing an operation
    messagebox.showinfo("Success", "Operation completed successfully.")

# Modern header style
header_label = tk.Label(root, text="", font=("Segoe UI", 24, "bold"), bg="#ffffff", fg="#333333")
header_label.grid(row=0, column=0, columnspan=3, pady=20)

# Create Source Directory input field and browse button
source_label = tk.Label(root, text="Source Directory:", font=("Segoe UI", 12), bg="#ffffff")
source_label.grid(row=1, column=0, sticky="w", padx=30, pady=10)

source_entry = ttk.Entry(root, width=50)
source_entry.grid(row=1, column=1, padx=30, pady=10)
source_browse_button = ttk.Button(root, text="Browse", command=lambda: browse_directory(source_entry))
source_browse_button.grid(row=1, column=2, padx=30, pady=10)

# Create Destination Directory input field and browse button
dest_label = tk.Label(root, text="Destination Directory:", font=("Segoe UI", 12), bg="#ffffff")
dest_label.grid(row=2, column=0, sticky="w", padx=30, pady=10)

dest_entry = ttk.Entry(root, width=50)
dest_entry.grid(row=2, column=1, padx=30, pady=10)
dest_browse_button = ttk.Button(root, text="Browse", command=lambda: browse_directory(dest_entry))
dest_browse_button.grid(row=2, column=2, padx=30, pady=10)

# Create Copy Type radio buttons
copy_type_label = tk.Label(root, text="Copy Type:", font=("Segoe UI", 12), bg="#ffffff")
copy_type_label.grid(row=3, column=0, sticky="w", padx=30, pady=10)

copy_type_var = tk.StringVar(value='files')  # Default selection is "Only Files"

# Reduced space by placing them on the same row and using a lower padx
radio_files = ttk.Radiobutton(root, text="Only Files", variable=copy_type_var, value="files")
radio_files.grid(row=3, column=1, sticky="w", padx=10, pady=5)  # Reduced padx and pady

radio_directory = ttk.Radiobutton(root, text="Entire Directory", variable=copy_type_var, value="directory")
radio_directory.grid(row=3, column=1, sticky="e", padx=10, pady=5)  # Aligned to the right of the same column


# Create Extensions input field (visible by default)
extensions_label = tk.Label(root, text="File Extensions (comma-separated):", font=("Segoe UI", 12), bg="#ffffff")
extensions_label.grid(row=4, column=0, sticky="w", padx=30, pady=10)

extensions_entry = ttk.Entry(root, width=50)
extensions_entry.grid(row=4, column=1, padx=30, pady=10)

# Checkbox for compression (only visible when 'directory' is selected)
compress_var = tk.BooleanVar(value=False)
compress_checkbox = ttk.Checkbutton(root, text="Compress before copying", variable=compress_var)

# Update visibility based on copy type
def on_copy_type_change():
    if copy_type_var.get() == "files":
        extensions_label.grid(row=4, column=0, sticky="w", padx=30, pady=10)
        extensions_entry.grid(row=4, column=1, padx=30, pady=10)
        compress_checkbox.grid_forget()
    else:
        extensions_label.grid_forget()
        extensions_entry.grid_forget()
        compress_checkbox.grid(row=4, column=0, columnspan=2, padx=30, pady=10)

copy_type_var.trace("w", lambda *args: on_copy_type_change())

# Create Start Button
start_button = ttk.Button(root, text="Start Copy", command=start_copy)
start_button.grid(row=5, column=0, columnspan=3, pady=30)

# Make sure the right column expands to fill the space
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=4)
root.grid_columnconfigure(2, weight=1)

# Run the GUI
root.mainloop()
