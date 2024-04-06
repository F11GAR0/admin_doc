import tkinter as tk
from tkinter import ttk, messagebox

from src.gui.users_form import UsersForm

class GeneralWindow(object):

    def __init__(self):

        self.parent = tk.Tk()
        self.parent.title("AdminDoc")
        self.parent.geometry("500x300")

        tabs = ttk.Notebook(self.parent)
        tab_users = tk.Frame(tabs)
        tab_roles = tk.Frame(tabs)
        tab_devices = tk.Frame(tabs)
        tab_services = tk.Frame(tabs)
        tabs.add(tab_users, text='Пользователи')
        tabs.add(tab_roles, text='Роли')
        tabs.add(tab_devices, text='Устройства')
        tabs.add(tab_services, text='Сервисы')

        self.tab_users_content = UsersForm(tab_users)

        tabs.pack(expand=1, fill="both")