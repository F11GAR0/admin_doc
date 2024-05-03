import tkinter as tk
from tkinter import ttk, messagebox

from src.gui.users_form import UsersForm
from src.gui.roles_form import RolesForm

class GeneralWindow():

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
        self.tab_roles_content = RolesForm(tab_roles)

        tabs.pack(expand=1, fill="both")