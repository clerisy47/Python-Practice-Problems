# Password-Manager-App
A password manager is an application that helps you securely store your login credentials for different websites and services. You only have to remember one password to access all the other passwords.

# Features
Store website, email/username and password
Generate random password
Search and retrieve login credentials
Copy password to clipboard

# Requirements
Python 3.x
tkinter
pyperclip
json

# Usage
Clone the repository and run main.py. The following functionalities are available:
Enter the website, email/username, and password and click "Add" to save the information to a JSON file.
Click "Generate Password" to generate a random password.
Enter the website and click "Search" to retrieve the saved login credentials for that website. The password will also be copied to the clipboard.

# Note
The project uses a JSON file to store the login credentials. The file is created in the same directory as main.py and is named data.json.
