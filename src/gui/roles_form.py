import tkinter as tk 

from src.lib.rdb.model import AuthError, database, auth

class RolesForm():

    def __init__(self, parent):

        self.parent = parent
        self.database = database
        self.root = tk.Frame(self.parent)

        header_users = tk.Label(self.root, text="Список пользователей")
        header_roles = tk.Label(self.root, text="Список ролей пользователя")

        self.users_list = tk.Listbox(self.root)
        self.roles_list = tk.Listbox(self.root)
        self.update_users()
        self.users_list.bind('<<ListboxSelect>>', self.update_roles)

        self.update_roles()


        self.button_add_user_role = tk.Button(self.root, text="Добавить", command=self.add_user_role)
        self.button_del_user_role = tk.Button(self.root, text="Удалить", command=self.del_user_role)

        header_users.grid(column=0, row=0)
        self.users_list.grid(column=0, row=1)
        header_roles.grid(column=1, row=0)
        self.roles_list.grid(column=1, row=1)
        self.button_add_user_role.grid(column=1, row=2)
        self.button_del_user_role.grid(column=1, row=3)

        self.root.pack(side="top", fill="x", padx=5, pady=15)

    def update_roles(self, event=None):

        if not hasattr(self, "roles_list"):
            return

        selection = self.users_list.curselection()

        if len(selection) <= 0:
            return

        user_index = int(selection[0])

        print(user_index)

        if user_index is None:
            return
        if user_index < 0:
            return

        user_id = database.users_get_all()[user_index][0]
        roles = database.roles_get_by_user(user_id)
        
        self.roles_list.delete(0, tk.END)
        
        for role in roles:
            self.roles_list.insert(tk.END, role[1])

    def update_users(self):

        if not hasattr(self, "roles_list"):
            return

        users = database.users_get_all()
        for user in users:
            self.users_list.insert(tk.END, user[1])

    def add_user_role(self):

        pass

    def del_user_role(self):

        pass