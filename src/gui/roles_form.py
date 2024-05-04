import tkinter as tk 

from src.lib.rdb.model import AuthError, database, auth


class AddUserPermissionForm():

    def __init__(self, parent, user_id):

        self.parent = parent
        self.database = database
        self.user_id = user_id
        self.root = tk.Toplevel(self.parent)

        header_roles = tk.Label(self.root, text="Список существующих ролей")
        self.roles_list = tk.Listbox(self.root)
        self.update_roles()
        self.add_button = tk.Button(self.root, text="Добавить", command=self.add_user_permission)

        header_roles.pack()
        self.roles_list.pack()
        self.add_button.pack()

    def update_roles(self, event=None):

        if not hasattr(self, "roles_list"):
            return

        roles = database.roles_get_all()
        
        self.roles_list.delete(0, tk.END)
        
        for role in roles:
            self.roles_list.insert(tk.END, role[1])

    def add_user_permission(self, event=None):

        selection = self.roles_list.curselection()

        if len(selection) <= 0:
            return

        role_index = int(selection[0])

        if role_index is None:
            return
        if role_index < 0:
            return

        role_id = database.roles_get_all()[role_index][0]
        database.roles_add_to_user(self.user_id, role_id)
        self.root.destroy()

class RolesForm():

    def __init__(self, parent: tk.Frame):

        self.parent = parent
        self.database = database
        self.root = tk.Frame(self.parent)

        header_users = tk.Label(self.root, text="Список пользователей")
        self.header_roles = tk.Label(self.root, text="*Нажмите на пользователя чтобы просмотреть роли.")

        self.users_list = tk.Listbox(self.root)
        self.roles_list = tk.Listbox(self.root)
        self.update_users()
        self.users_list.bind('<<ListboxSelect>>', self.update_roles)

        self.last_selected_user_id = None
        self.last_selected_role_id = None

        self.update_roles()

        self.button_add_user_role = tk.Button(self.root, text="Добавить", command=self.add_user_permission)
        self.button_del_user_role = tk.Button(self.root, text="Удалить", command=self.del_user_permission)

        header_users.grid(column=0, row=0)
        self.users_list.grid(column=0, row=1)
        self.header_roles.grid(column=1, row=0)
        self.roles_list.grid(column=1, row=1)
        self.button_add_user_role.grid(column=1, row=2)
        self.button_del_user_role.grid(column=1, row=3)

        self.root.pack(side="top", fill="x", padx=5, pady=15)

    def _get_selected_user_id(self):

        if not hasattr(self, "users_list"):
            return None

        selection = self.users_list.curselection()

        if len(selection) <= 0:
            return None

        user_index = int(selection[0])

        if user_index is None:
            return None
        if user_index < 0:
            return None

        user_id = database.users_get_all()[user_index][0]
        self.last_selected_user_id = user_id

        return user_id

    def _get_selected_role_id(self):

        if not hasattr(self, "roles_list"):
            return

        selection = self.roles_list.curselection()

        if len(selection) <= 0:
            return None

        role_alias = self.roles_list.selection_get()

        if role_alias is None:
            return None

        role_id = database.roles_get_by_alias(alias=role_alias)[0][0]
        self.last_selected_role_id = role_id

        return role_id

    def update_users(self, event=None):

        if not hasattr(self, "roles_list"):
            return
        
        self.users_list.delete(0, tk.END)
        
        users = database.users_get_all()
        for user in users:
            self.users_list.insert(tk.END, user[1])

    def update_roles(self, event=None):
        
        user_id = self._get_selected_user_id()

        if user_id is None:
            
            if (user_id := self.last_selected_user_id) is None:

                return

        roles = database.roles_get_by_user(user_id)
        
        self.roles_list.delete(0, tk.END)
        self.header_roles.configure(text="Список прав пользователя")
        for role in roles:
            self.roles_list.insert(tk.END, role[1])

    def add_user_permission(self):

        user_id = self._get_selected_user_id()

        if user_id is None:
            
            if (user_id := self.last_selected_user_id) is None:

                return

        add_user = AddUserPermissionForm(self.root, user_id)
        add_user.root.bind("<Destroy>", self.update_roles)

    def del_user_permission(self):

        role_id = self._get_selected_role_id()

        if role_id is None:

            if (role_id := self.last_selected_role_id) is None:

                return
        
        user_id = self._get_selected_user_id()

        if user_id is None:

            if (user_id := self.last_selected_user_id) is None:

                return

        print(f"uid: {user_id} | rid: {role_id}")

        database.roles_del_from_user(user_id, role_id)

        self.update_roles()