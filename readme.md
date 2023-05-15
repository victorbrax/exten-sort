<div align="center">
  <table>
  <tr>
    <td><img height="24rem" src="https://raw.githubusercontent.com/victorbrax/filebrax-hub/c65a8072294d7b044a5909e03bcb0e7a7dcf6e3c/docs/br.svg" alt="brazilflag"></td>
    <td>Você fala Português? Por favor, <a href="https://github.com/victorbrax/tracker-tickets/blob/main/docs/LEIAME.md">clique aqui</a>.</td>
  </tr>
</table>
</div>

<div align="center">
  
[![Project](https://img.shields.io/badge/PERSONAL_PROJECT-important.svg)]()
[![Python](https://img.shields.io/badge/Python-informational.svg)]()
[![Pandas](https://img.shields.io/badge/Pandas-green.svg)]()
[![Openpyxl](https://img.shields.io/badge/Openpyxl-gray.svg)]()
</div>


<div align="center">
<img width="100%" src="https://raw.githubusercontent.com/victorbrax/exten-sort/main/docs/logos/extensort-logo.png">
</div>
</div>
<p align="center">By <strong>Víctor Gomes</strong></p>

# Greetings! ⚜

Always been obsessed with **organization**, keeping things in their proper places following best practices. It has always been crucial to me. Moreover, there's no price tag on the pleasure of quickly finding the desired file by looking in the right place. That's why I developed an application that automatically organizes my `Downloads folder` **when the computer is turned on**.
</br>
</br>

## Demo 🖼️

<div align="center">
<img height="400vh" src="https://raw.githubusercontent.com/victorbrax/tracker-tickets/main/docs/images/example.png">
</div>

## Run Project Locally 🏠

Assumes local installation of [Python](https://python.org/downloads) to run the project locally:

* Clone or fork this repository.
* Create a virtual environment. You can do this by using `python -m venv venv` in the terminal.
* Install the necessary libraries. If you use pip to manage your packages, use `pip install -r requirements.txt`.
* Run `python app.py`
* Check the file `Tracker Tickets.xlsx` appearing at the project's root path.

## Technologies Used 🖥️
* [Pandas](https://pandas.pydata.org/)
* [Openpyxl](https://openpyxl.readthedocs.io/en/stable/)
* [Jinja2](https://palletsprojects.com/p/jinja/)

## Considerations 📝
> The first Tracker had a rather rudimentary interface made with Tkinter. Additionally, it didn't format the spreadsheets with colors and didn't delete old columns. Subsequently, the decision was made to remove the visual interface, simplifying the execution process by eliminating the dialog boxes for file selection. This was done to enhance the understanding and usability of the Tracker.

* Obviously, the spreadsheets in the sheetfiles folder are very basic examples since the actual files are private and **cannot be published**.
* You can adapt it for larger datasets, specify the columns you want to exclude, and add more merges.
* You can easily change the colors by modifying the `hexadecimal codes` in the styling calls.

## License 📜

The code in this project is licensed under the MIT License. See [LICENSE](LICENSE) for details.</br>

> Thank you for the prestige. 🐍





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

### Idea
You can place the ExtenSort code to be executed automatically every time you start your computer? By placing the code in the "Startup" folder on Windows, it will run every time you log in. To do this, you can follow these steps:

1.  Create an executable of the ExtenSort code using Pyinstaller
2.  Open the Run dialog box by pressing the Windows key + R
3.  Type shell:startup and press Enter
4.  This will open the Startup folder in File Explorer
5.  Place the executable of the ExtenSort code here.

The path of the Startup folder is typically "C:\Users\YourUsername\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

By adding the ExtenSort code to the Startup folder, you can ensure that your downloads are always organized and sorted by extension, without having to manually run the code every time. With this setup, the code will run automatically every time you turn on your computer, giving you the peace of mind that your downloads are always organized.

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

### Disclaimer
Use the script at your own risk. It is important to test it on a small folder before running it on the entire downloads folder to make sure it works correctly and to avoid any data loss.

> Thank you for the prestige.

