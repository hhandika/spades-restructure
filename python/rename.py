import os
import glob
import argparse

# Read directory and find files with extension
def find_files(directory, extension):

    # Use glob to find files with the specified extension
    if not directory or not extension:
        raise ValueError("Both 'directory' and 'extension' must be provided and non-empty.")
    path = os.path.abspath(directory)
    glob_pattern = os.path.join(path, f"*.{extension.lower()}")
    print(f"Searching for files in '{path}' with pattern '{glob_pattern}'")
    if not os.path.exists(path):
        raise FileNotFoundError(f"The directory '{path}' does not exist.")
    files = glob.glob(glob_pattern)
    
    # Print the list of files found
    print(f"Files with extension '{extension}': {files}")
    
    return files

# Extract file name and extension
def extract_name_and_extension(file_path):
    # Split the file path into name and extension
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    
    # Print the extracted name and extension
    print(f"Extracted name: {name}, extension: {ext}")
    
    return name, ext

# Use the file name as a folder name 
# and extension as a file name
# Use fasta as an extension
def rename_files(files):
    for file_path in files:
        # Extract the name and extension
        name, ext = extract_name_and_extension(file_path)
        
        # Create a folder with the name
        folder_name = name
        os.makedirs(folder_name, exist_ok=True)

        # remove dot from the extension
        ext = ext.lstrip('.')
        
        # Move the file into the folder with the new name
        new_file_path = os.path.join(folder_name, f"{ext}.fasta")
        os.rename(file_path, new_file_path)
        
        # Print the new file path
        print(f"Renamed '{file_path}' to '{new_file_path}'")

def main():
    # Add argument for input dir
    parser= argparse.ArgumentParser(description="Rename files and move them into folders.")
    parser.add_argument("--ext", type=str, help="File extension to search for")
    parser.add_argument("--dir", type=str, help="Directory to search in")
    
    # Parse the arguments
    args = parser.parse_args()
    extension = args.ext
    directory = args.dir

    files = find_files(directory, extension)
    if not files:
        print(f"No files found with extension '{extension}'")
        return
    rename_files(files)

if __name__ == "__main__":
    main()
