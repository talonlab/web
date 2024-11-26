import os


def rename_files_in_folder(folder_path):
  try:
    # Check if the folder exists
    if not os.path.exists(folder_path):
      print(f"The folder '{folder_path}' does not exist.")
      return

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
      # Construct the full file path
      old_file_path = os.path.join(folder_path, filename)

      # Skip directories
      if not os.path.isfile(old_file_path):
        continue

      # Create the new filename
      new_filename = filename.lower().replace(' ', '-')
      new_file_path = os.path.join(folder_path, new_filename)

      # Rename the file
      os.rename(old_file_path, new_file_path)
      print(f"Renamed: {filename} -> {new_filename}")

    print("File renaming complete.")
  except Exception as e:
    print(f"An error occurred: {e}")


# Example usage
# Replace 'your/folder/path' with the actual folder path
folder_path = '/'
rename_files_in_folder(folder_path)
