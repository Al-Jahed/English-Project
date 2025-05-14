import os
import streamlit as st


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


# Streamlit app setup
st.title("Folder Search Tool")

# Input for base directory
base_dir = st.text_input("Enter the base directory:", "")
if not base_dir:
    st.warning("Please enter a base directory.")

# Input for search query
query = st.text_input("Enter topic or path to search:", "")
if st.button("Search"):
    if not base_dir:
        st.error("No base directory provided. Please enter one.")
    elif not os.path.isdir(base_dir):
        st.error("The base directory does not exist. Please enter a valid directory.")
    elif not query:
        st.warning("Please enter a topic name or path.")
    else:
        # Normalize and split the query into path parts
        path_parts = query.replace("\\", "/").split("/")
        matching_folders = find_all_matching_paths(base_dir, path_parts)

        if not matching_folders:
            st.error(f"No matching folder found for '{query}'.")
        else:
            # Collect all files from matching folders
            all_files = []
            for folder in matching_folders:
                all_files.extend(list_files_in_subfolders(folder))

            if not all_files:
                st.warning(f"No files found in the matching folders for '{query}'.")
            else:
                st.success(f"Found {len(all_files)} files matching your query.")
                for file in all_files:
                    st.text(file)