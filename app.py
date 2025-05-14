import os
import tkinter as tk
from tkinter import filedialog, messagebox


def find_all_matching_paths(base_dir, path_parts):
    """
    Recursively searches for folders matching the given path parts.
    """
    matching_paths = []

    def search_directory(current_dir, parts):
        if not parts:
            matching_paths.append(current_dir)
            return

        next_part = parts[0]
        for item in os.listdir(current_dir):
            item_path = os.path.join(current_dir, item)
            if os.path.isdir(item_path):
                # Check if the current folder matches the query part
                if next_part.lower() in item.lower():
                    search_directory(item_path, parts[1:])
                # Continue traversing even if it doesn't match
                search_directory(item_path, parts)

    search_directory(base_dir, path_parts)
    return matching_paths


def list_files_in_subfolders(folder):
    """
    Lists all files in the given folder and its subfolders.
    """
    file_list = []
    for root, _, files in os.walk(folder):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


def on_search(event=None):
    """
    Handles the search functionality when the user enters a query.
    """
    query = topic_entry.get().strip()
    if not query:
        messagebox.showwarning("Input Required", "Please enter a topic name or path.")
        return

    # Normalize and split the query into path parts
    path_parts = query.replace("\\", "/").split("/")
    matching_folders = find_all_matching_paths(BASE_DIR, path_parts)

    # Clear the result listbox
    result_listbox.delete(0, tk.END)

    if not matching_folders:
        messagebox.showerror("Not Found", f"No matching folder found for '{query}'.")
        result_listbox.insert(tk.END, f"⚠ No folder found matching: '{query}'")
        return

    # Collect all files from matching folders
    all_files = []
    for folder in matching_folders:
        all_files.extend(list_files_in_subfolders(folder))

    if not all_files:
        result_listbox.insert(tk.END, f"⚠ No files found in: '{query}'")
    else:
        for file in all_files:
            result_listbox.insert(tk.END, file)


# Prompt user to select a base directory
root = tk.Tk()
root.withdraw()  # Hide the root window while selecting the directory
BASE_DIR = filedialog.askdirectory(title="Select Base Directory")
if not BASE_DIR:
    messagebox.showerror("Error", "No directory selected. Exiting program.")
    exit()

# GUI Setup
root = tk.Tk()
root.title("Folder Search Tool")

# Input field
tk.Label(root, text="Enter Topic or Path:").pack(pady=5)
topic_entry = tk.Entry(root, width=50)
topic_entry.pack(pady=5)
topic_entry.bind("<Return>", on_search)

# Search button
search_button = tk.Button(root, text="Search", command=on_search)
search_button.pack(pady=5)

# Results listbox
result_listbox = tk.Listbox(root, width=80, height=20)
result_listbox.pack(pady=10)

# Start the GUI loop
root.mainloop()
