import tkinter as tk 

from src.lib.rdb.model import AuthError, database, auth

class RolesForm():

    def __init__(self, parent):

        self.parent = parent
        self.database = database
        self.root = tk.Frame(self.parent)

        self.header = tk.Label(self.root, text="Список ролей")
        self.header.pack()
        self.root.pack(side="top", fill="x", padx=5, pady=15)