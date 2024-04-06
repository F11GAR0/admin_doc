import tkinter as tk
import tksheet
from tkinter import ttk, messagebox

from src.lib.rdb.model import database

class UsersForm(object):

    def __init__(self, parent):

        self.parent = parent
        self.database = database
        self.root = tk.Frame(self.parent, background="gray", padx=5, pady=15)

        self.table = tksheet.Sheet(self.root, "Список пользователей")
        self.table.set_sheet_data(data=database.users_get_all())
        self.table.enable_bindings(("single_select",
                                    "row_select",
                                    "column_width_resize",
                                    "arrowkeys",
                                    "right_click_popup_menu",
                                    "rc_select",
                                    "rc_delete_row",
                                    "copy"))
        self.table.pack(fill="x")

        self.button_container = tk.Frame(self.root, height=15)

        self.button_delete = tk.Button(self.button_container, text="Удалить", command=self.delete_user)
        self.button_delete.grid(column=0, row=0)
        self.button_add = tk.Button(self.button_container, text="Добавить", command=self.add_user)
        self.button_add.grid(column=1, row=0)
        self.button_container.pack()

        self.root.pack(side="top", fill="x")

    def delete_user(self):

        pass

    def add_user(self):

        pass