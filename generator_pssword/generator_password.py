import string
from random import randint,choice
from tkinter import *


def generator_password():
    password_min=6
    password_max=12
    all_chars=string.ascii_letters + string.punctuation + string.digits
    password="".join(choice(all_chars) for x in range(randint(password_min,password_max)))
    Password.delete(0,END)
    Password.insert(0,password)

window=Tk()

window.title("generateur de password")
window.config(background='white')
window.geometry("1080x760")

frame = Frame(window, bg='#41b77F')

right_frame=Frame(frame, bg='#41b77F')

label_title = Label(right_frame,text="generateur de mot de passe", font="Algerian" , bg='#41b77F', fg='white')
label_title.pack()
Password = Entry(right_frame, font="Algerian" , bg='#41b77F', fg='white')
Password.pack()
password_button = Button(right_frame,text="generer", font="Algerian" , bg='#41b77F', fg='white',command=generator_password)
password_button.pack()
right_frame.pack()
frame.pack(expand=YES)
menu=Menu(window)
menu_file=Menu(window,tearoff=0)
menu_file.add_command(label="new",command=generator_password)
menu_file.add_command(label="Leave",command=window.quit)
menu.add_cascade(label="file",menu=menu_file)
window.config(menu=menu)
mainloop()