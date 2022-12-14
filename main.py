from tkinter import *
# Messagebox is not a direct class of tkinter so, it has to be import it everytime
from tkinter import messagebox
from random import randint, choice, shuffle
# Pyperclip allows copy user's input
import pyperclip
import json
# ___________________________________ PASSWORD GENERATOR ________________________________________#


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    # The join method will concatenate all the elements of our password_list (We can also add elements between the "")
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ____________________________________ SAVE PASSWORD ______________________________________________#


def save():
    web = website_entry.get()
    email = username_entry.get()
    passwords = password_entry.get()
    new_data = {
        web: {
            "email": email,
            "password": passwords
        }
    }

    if len(web) == 0 or len(passwords) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # is_ok = messagebox.askokcancel(title=web,
        #                                message=f"These are the details entered: \n{email} \nPassword: {passwords}"
        #                                        f" \nIs it ok to save?")
        try:
            with open("data.json", "r") as data_file:
                """The code below allows to read data from a Json file"""
                data = json.load(data_file)
                """The code below allows to update a Json file"""
                data.update(new_data)
                """The code below saves the updated data"""
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as updated_data:
                """The code below writes data to file in the Json form"""
                json.dump(data, updated_data, indent=4)
            """Erases user's input"""
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# _____________________________________ UI SETUP ___________________________________________________#
"""Window"""
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
"""Canvas"""
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)
"""Labels"""
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
"""Entries"""
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
# Allows cursor to start at entry box
website_entry.focus()
username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "resolute@email.com")
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)
"""Buttons"""
generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(row=3, column=2)
add_password = Button(text="Add", width=44, command=save)
add_password.grid(row=4, column=1, columnspan=2)


window.mainloop()
