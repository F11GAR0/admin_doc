import tkinter as tk
from tkinter import ttk

from src.gui.users_form import UsersForm
from src.gui.roles_form import RolesForm
from src.gui.devices_form import DevicesForm
from src.gui.services_form import ServicesForm

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
        self.tab_devices_content = DevicesForm(tab_devices)
        self.tab_services_content = ServicesForm(tab_services)
        tabs.bind('<<NotebookTabChanged>>', self._update_tabs)
        tabs.pack(expand=1, fill="both")

    def _update_tabs(self, event=None):

        self.tab_roles_content.update_users()
        self.tab_devices_content.update_users()
        self.tab_services_content.update_users()