import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

YELLOW = "#FFFEA9"
NAVY = "#0F2C67"
PINK = "#FD6F96"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    # This will help to copy the password immediately after it is generated and to paste it elsewhere.
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data_dict = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            # Reading old data from the JSON file if the file exist
            with open("passwords.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # Creating and writing the data to JSON file
            with open("passwords.json", "w") as data_file:
                json.dump(new_data_dict, data_file, indent=4)
        else:
            # Updating the data with new data
            data.update(new_data_dict)
            # writing the updated data to JSON file
            with open("passwords.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No File With Website Details Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            pyperclip.copy(password)
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details found for {website} website")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(height=200, width=200, bg=YELLOW, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg=YELLOW)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg=YELLOW)
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg=YELLOW)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "niharika123@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password, bg=PINK, fg=NAVY)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=45, command=save, bg=PINK, fg=NAVY)
add_button.grid(row=4, column=1, columnspan=2)
search_password_button = Button(text="Search", width=14, bg=PINK, fg=NAVY, command=search_password)
search_password_button.grid(row=1, column=2)

window.mainloop()
