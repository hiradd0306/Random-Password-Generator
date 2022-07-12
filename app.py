from generator import generate_password
import tkinter as tk
from tokenize import Name

app = tk.Tk()
app.geometry("500x300")
app.title("Random Password Generator")

title_label = tk.Label(text="Random Password Generator", font='Helvetica 24 bold')
title_label.grid(column=0, row=0, pady=20)

text_label = tk.Label(text="Enter the desired length of your password:")
text_label.grid(column=0, row=1)

length_entry = tk.Entry()
length_entry.grid(column=0, row=2)

enter_button = tk.Button(
    text="Enter", 
    command=lambda:button_click_enter(length_entry.get()))
enter_button.grid(column=1,row=2)

error_text = tk.StringVar()
password_text = tk.StringVar()

password_label = tk.Label(text=password_text)
password_label.grid(column=0, row=4)
error_label = tk.Label(text=error_text)
error_label.grid(column=0, row=5)


def button_click_enter(length):
    global error_text
    global password_text
    
    try: 
        length = int(length)
        
        if length < 7:
            raise ValueError
    except ValueError:
        if type(length) == int:
            error_text.set("Password has to be at least 8 characters.")
        else:
            error_text.set("Please enter a valid password.")
        password_label.grid_forget()
    else: 
        password_text.set(generate_password(length))
        error_label.grid_forget()
    
app.mainloop()