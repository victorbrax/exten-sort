<div align="center">
  <table>
  <tr>
    <td><img height="24rem" src="https://raw.githubusercontent.com/victorbrax/filebrax-hub/c65a8072294d7b044a5909e03bcb0e7a7dcf6e3c/docs/br.svg" alt="brazilflag"></td>
    <td>Você fala Português? Por favor, <a href="https://github.com/victorbrax/exten-sort/blob/main/docs/LEIAME.md">clique aqui</a>.</td>
  </tr>
</table>
</div>

<div align="center">
  
[![Project](https://img.shields.io/badge/PERSONAL_PROJECT-important.svg)]()
[![Python](https://img.shields.io/badge/Python-informational.svg)]()
[![auto-py-to-exe](https://img.shields.io/badge/Auto_Py_to_Exe-green.svg)]()
[![OS](https://img.shields.io/badge/OS-gray.svg)]()
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
<img height="400vh" src="https://raw.githubusercontent.com/victorbrax/exten-sort/main/docs/images/example-photo.png">
</div>

## Run Project Locally (No Python Installed) 🏠

This project has an executable file, so if you are an inexperienced user with programming or a lazy developer, you can simply download it and follow the steps below.

* Download _**.exe**_ `exten-sort` in [dist](dist) folder.
* Press `Win + R` and type `shell:startup`
* Move the executable to the folder and be happy.

## Run Project Locally (Python Installed) 🏠

Assumes local installation of [Python](https://python.org/downloads) to run the project locally:

* Clone or fork this repository.
* Create a virtual environment. You can do this by using `python -m venv venv` in the terminal.
* Install the necessary libraries. If you use pip to manage your packages, use `pip install -r requirements.txt` (in case you want to create the installer later).
* Run `auto-py-to-exe` in the terminal, choose "One File", use the icon in [icons folder](docs/icons), and generate your executable file.
* Run `python main.pyw`
* Check your `Downloads folder`.

## Technologies Used 🖥️
* [Shutil](https://docs.python.org/3/library/shutil.html)
* [OS](https://docs.python.org/3/library/os.html)
* [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe)

## Considerations 📝
* This project scans your Downloads folder and checks the extension of each file. After that, it creates a folder (if it doesn't already exist) and moves the file into it, making everything more organized. 
* This application helps me keep my downloads folder organized on a daily basis, and I hope it helps you too. You can change the target directory to another one if needed.
* There are other similar projects on the internet, but I decided to create my own because I wanted a more concise and efficient code, especially for handling less commonly known file extensions.

## License 📜

The code in this project is licensed under the MIT License. See [LICENSE](LICENSE) for details.</br>

> Thank you for the prestige. 🐍
