import tkinter as tk
from tkinter import messagebox, StringVar

from src.gui.general_form import GeneralWindow
from src.lib.rdb.model import Database
from src.lib.crypt.hash import validate_password

class LoginWindow(object):

    def __init__(self, database: Database):

        self.parent = tk.Tk()
        self.parent.title("Login to AdminDoc")
        self.parent.geometry("100x50")
        self.database = database
        
        username_label = tk.Label(self.parent, text="Email:")
        username_label.pack()

        self.username_entry = tk.Entry(self.parent)
        self.username_entry.pack()

        password_label = tk.Label(self.parent, text="Пароль:")
        password_label.pack()

        self.password_entry = tk.Entry(self.parent, show="*")  # Show asterisks for password
        self.password_entry.pack()

        login_button = tk.Button(self.parent, text="Войти", command=self.validate_login)
        login_button.pack()

        self.message = StringVar()
        self.message_label = tk.Label(self.parent, textvariable=self.message)
        self.message_label.pack()


    def validate_login(self):

        user_id = self.database.users_get_id_by_email(self.username_entry.get())
        user_password_hash = self.database.users_passwd_get_by_id(user_id)

        if validate_password(self.password_entry.get(), user_password_hash):
            
            self.message.set("Success.")

            window = GeneralWindow()
            self.parent.destroy()
            self.parent = window.parent

        else:

            self.message.set("Wrong email or password. Try again.")
