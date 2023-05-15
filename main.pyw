import os
from shutil import move

# Define the "path" variable as the user's downloads folder
path = os.path.expanduser("~/Downloads")

# Start a loop to go through all files in the downloads folder
for file in os.listdir(path):
    # Check if the current item is a file and not a folder
    if os.path.isfile(os.path.join(path, file)):
        # Check if the file has an extension
        if '.' in file:
            # Get the extension of the current file
            extension = file.split(".")[-1]
        else:
            # Skip the file if it doesn't have an extension
            continue

        # Create the path for the folder with the current file's extension
        extension_path = os.path.join(path, extension)

        # Check if the folder with the current file's extension already exists. If it doesn't, create a new folder with the extension's name
        if not os.path.exists(extension_path):
            os.mkdir(extension_path)

        # Move the current file to the folder with its corresponding extension
        move(os.path.join(path, file), os.path.join(extension_path, file))