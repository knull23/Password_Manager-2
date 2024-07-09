from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import pyperclip


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for j in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for k in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    new_website = website_entry.get()
    new_email = email_entry.get()
    new_password = password_entry.get()

    if len(new_website) == 0 or len(new_password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't"
                                                   "left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=new_website, message=f"These are the "
                                                                  f"details entered:"
                                                          f" \nEmail: {new_email} \nPassword:"
                                                          f" {new_password} \nIs it okay to save?")

        if is_ok:
            with open('data.txt', 'a') as f:
                f.write(f"{new_website} | {new_email} | {new_password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "angela@gmail.com")

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

password_generate_btn = Button(text="Generate Password", width=14, command=generate_password)
password_generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=30, command=save)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()