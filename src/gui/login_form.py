import tkinter as tk
from tkinter import StringVar

from src.gui.general_form import GeneralWindow
from src.lib.rdb.model import AuthError, auth

class LoginWindow():

    def __init__(self):

        self.parent = tk.Tk()

        self.login_box = tk.Frame(self.parent, width=100, height=50, padx=5, pady=5)

        self.parent.title("Login to AdminDoc")
        
        username_label = tk.Label(self.login_box, text="Логин:", pady=3)
        username_label.pack()

        self.username_entry = tk.Entry(self.login_box)
        self.username_entry.pack()
        self.username_entry.bind('<FocusIn>', self.on_entry_click)
        self.username_entry.bind('<FocusOut>', self.on_focusout)
        self.username_entry.insert(0, 'email@mail.com')

        password_label = tk.Label(self.login_box, text="Пароль:",pady=3)
        password_label.pack()

        self.password_entry = tk.Entry(self.login_box, show="*")  # Show asterisks for password
        self.password_entry.pack()

        login_button = tk.Button(self.login_box, text="Войти", command=self.validate_login, pady=3)
        login_button.pack(pady=10)

        self.message = StringVar()
        self.message_label = tk.Label(self.login_box, textvariable=self.message, pady=10)
        self.message_label.pack()

        self.login_box.place(in_=self.parent, anchor="c", relx=.5, rely=.5)

    def on_entry_click(self, event):

        """function that gets called whenever entry is clicked"""
        if self.username_entry.get() == 'email@mail.com':
            self.username_entry.delete(0, "end") # delete all the text in the entry
            self.username_entry.insert(0, '') #Insert blank for user input
            self.username_entry.config(fg = 'black')

    def on_focusout(self, event):
        if self.username_entry.get() == '':
            self.username_entry.insert(0, 'email@mail.com')
            self.username_entry.config(fg = 'grey')

    def validate_login(self):

        try:
            auth.validate_login(self.username_entry.get(), self.password_entry.get())
            self.message.set("Success.")

            window = GeneralWindow()
            self.parent.destroy()
            self.parent = window.parent
        except AuthError as e:
            self.message.set(str(e))
    