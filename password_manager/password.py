from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def create_pass():
    restart()
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for i in range(nr_letters)]
    password_list += [random.choice(symbols) for i in range(nr_symbols)]
    password_list += [random.choice(numbers) for i in range(nr_numbers)]
    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_input.insert(0, string=f"{password}")
    pyperclip.copy(f"{password}")



# ---------------------------- SAVE PASSWORD ------------------------------- #

def restart():
    password_input.delete(0, 'end')
    web_input.delete(0, 'end')
    web_input.focus()


def add_info():
    # info grab
    email_capture = email_username_input.get()
    website_capture = web_input.get()
    password_capture = password_input.get()

    if len(website_capture) == 0:
        print("web entry is empty")
        messagebox.showerror(title="Ooops", message="You have a field that is not filled out")
        restart()

    elif len(password_capture) == 0:
        print("password entry is empty")
        messagebox.showerror(title="Ooops", message="You have a field that is not filled out")
        restart()
    else:
        is_ok = messagebox.askokcancel(title=f"{website_capture}", message=f"These are the details entered\n"
                                                                           f"Email: {email_capture}\n"
                                                                           f"Password: {password_capture}\n"
                                                                           f"Is this okay to save?")

        if is_ok:
            # appending info to existing/new file
            my_private_info = open("data.txt", "a")
            my_private_info.write(f"{website_capture}  |  {email_capture}  |  {password_capture} \n")
            my_private_info.close()
            restart()
        else:
            restart()

# ---------------------------- UI SETUP ------------------------------- #

# SCREEN SETTINGS


pop_screen = Tk()
pop_screen.title(string="                                                  Password Manager")

pop_screen.config(padx=50, pady=50)


# CANVAS SETTINGS
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# LABELS
website_label = Label(text='Website: ')
website_label.grid(row=1, column=0)

email_username_label = Label(text='Email/Username: ')
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# INPUTS
web_input = Entry(width=35)
web_input.grid(row=1, column=1, columnspan=2)
web_input.focus()

email_username_input = Entry(width=35)
email_username_input.grid(row=2, column=1, columnspan=2)
email_username_input.insert(0, "carlos.oran15@hotmail.com")

password_input = Entry(width=35)
password_input.grid(row=3, column=1, columnspan=2)

# BUTTONS
create_pass_button = Button(text="Generate password", command=create_pass)
create_pass_button.grid(row=4, column=1)

add_button = Button(text="Add", width=30, command=add_info)
add_button.grid(row=5, column=1, columnspan=2)

pop_screen.mainloop()
