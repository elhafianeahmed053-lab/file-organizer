import os
import shutil

folder_path = os.getcwd()

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Split filename and extension
    name, ext = os.path.splitext(file)

    # Files with no extension go to "no_extension"
    if ext == "":
        folder_name = "no_extension"
    else:
        folder_name = ext[1:]  # remove the dot

    destination_folder = os.path.join(folder_path, folder_name)
    os.makedirs(destination_folder, exist_ok=True)

    destination_path = os.path.join(destination_folder, file)

    # Skip if already in correct place
    if file_path == destination_path:
        continue

    shutil.move(file_path, destination_path)

print("Files organized successfully!")
