from tkinter import *
from tkinter import messagebox
from random_password_generator import *
import pyperclip
import json


def save_to_file():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    data_dict = {website: {
        "Email": email,
        "Password": password
    }}
    if email == "" or password == "" or website == "":
        messagebox.showerror(title="Invalid entry", message="You can't leave the entry fields empty")
        return NONE
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            data.update(data_dict)
    except json.decoder.JSONDecodeError:
        with open("data.json", "w") as f:
            json.dump(data_dict, f, indent=4)
    else:
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
    pyperclip.copy(password)
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def generate():
    random_password = random_password_generator()
    password_entry.insert(0, random_password)


def search():
    website = website_entry.get()
    with open("data.json", "r") as f:
        try:
            data = json.load(f)
            messagebox.showinfo(title=website,
                                message=f"Email: {data[website]['Email']}\nPassword: {data[website]['Password']}")
        except (KeyError, json.decoder.JSONDecodeError):
            messagebox.showwarning(title="Not Found", message=f"{website}'s login data hasn't been recorded yet")
        else:
            pyperclip.copy(data[website]["Password"])
        website_entry.delete(0, END)
        password_entry.delete(0, END)


tk = Tk()
tk.config(padx=20, pady=20)

image = PhotoImage(file="./logo.png")
label = Label(tk, image=image, width=200, height=200)
label.grid(row=0, column=1)

label = Label(tk, text="Website:")
label.grid(row=1, column=0)
website_entry = Entry(tk, width=19)
website_entry.grid(row=1, column=1)
website_entry.focus()
button_search = Button(tk, text="Search", width=12, command=search)
button_search.grid(row=1, column=2)

label = Label(tk, text="Email/Username:")
label.grid(row=2, column=0)
email_entry = Entry(tk, width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "acharya.utsav100@gmail.com")

label = Label(tk, text="Password:")
label.grid(row=3, column=0)
password_entry = Entry(tk, width=19)
password_entry.grid(row=3, column=1)
button = Button(tk, text="Generate Password", width=12, command=generate)
button.grid(row=3, column=2)

button = Button(tk, text="Add", width=33, command=save_to_file)
button.grid(row=4, column=1, columnspan=2)

tk.mainloop()
