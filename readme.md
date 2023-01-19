## ExtenSort

An application that automatically organizes and sorts files in the downloads folder by extension.

### Usage

1.  Make sure you have python installed in your computer.
   
2.  Download or clone the code to your computer.
    
3.  Open a terminal and navigate to the folder where the code is located.
    
4.  Run the command

	`python extensort.py` 

6.  The script will run and create folders for each different file extension found in the downloads folder. The files will be moved to the corresponding folders.
    
7.  Done! your downloads folder should be organized now.

### Note

This script was tested on Windows, if you're using other OS some adjustments on the path to the downloads folder may be required. Also, it's important to notice that some systems may require additional libraries to be installed.

If you have any question or problem feel free to open an issue or contact me.

### Disclaimer

Use the script at your own risk. It is important to test it on a small folder before running it on the entire downloads folder to make sure it works correctly and to avoid any data loss.

### Step-by-step explanation

`import os from shutil import move` 

Import the "os" and "shutil" libraries, which will be used to navigate and move files in the download folder.

`path = os.path.expanduser("~/Downloads")`

Define the "path" variable as the user's download folder. The "os.path.expanduser" method is used to get the full path of the download folder.

`for file in os.listdir(path):`

Starts a loop to go through all files in the download folder. The "os.listdir" method is used to get a list of all files in the folder.

`if os.path.isfile(os.path.join(path, file)):`

Checks if the current file is actually a file and not a folder. The "os.path.isfile" method is used to check if the specified path is a file.

`extension = file.split(".")[-1]`

Gets the extension of the current file. The "file.split" method is used to split the file name into a list of strings, based on the "." separator. The last item in the list is the file extension.

`extension_path = os.path.join(path, extension)`

Creates the path to the folder with the current file's extension. The "os.path.join" method is used to join the download folder path with the extension name.

`if not os.path.exists(extension_path): os.mkdir(extension_path)`

Checks if the folder with the current file's extension already exists. If it does not exist, a new folder with the extension name is created.

`move(os.path.join(path, file), os.path.join(extension_path, file))`

Moves the current file to the folder with its corresponding extension. The "move" method from the "shutil" library is used to move the file from one place to.

> Thank you for the prestige.

