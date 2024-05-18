import tkinter as tk 
from tkinter import messagebox

from src.lib.rdb.model import database


class AddUserServiceForm():

    def __init__(self, parent, user_id):

        self.parent = parent
        self.database = database
        self.user_id = user_id
        self.root = tk.Toplevel(self.parent)

        header_services = tk.Label(self.root, text="Список существующих сервисов")
        self.services_list = tk.Listbox(self.root)
        self.update_services()
        self.add_button = tk.Button(self.root, text="Добавить", command=self.add_service)

        header_services.pack()
        self.services_list.pack()
        self.add_button.pack()

    def update_services(self, event=None):

        if not hasattr(self, "services_list"):
            return

        services = database.services_get_all()
        
        self.services_list.delete(0, tk.END)
        
        for service in services:
            self.services_list.insert(tk.END, service[1])

    def add_service(self, event=None):

        selection = self.services_list.curselection()

        if len(selection) <= 0:
            return

        service_index = int(selection[0])

        if service_index is None:
            return
        if service_index < 0:
            return

        service_id = database.services_get_all()[service_index][0]
        database.services_add_to_user(self.user_id, service_id)
        self.root.destroy()


class AddServiceForm():

    def __init__(self, parent):

        self.parent = parent
        self.database = database
        self.root = tk.Toplevel(self.parent)

        header_alias = tk.Label(self.root, text="Псевдоним")
        self.tb_alias = tk.Entry(self.root)
        header_fqdn = tk.Label(self.root, text="FQDN (Domain name)")
        self.tb_fqdn = tk.Entry(self.root)

        self.add_button = tk.Button(self.root, text="Добавить", command=self.add_service)

        header_alias.pack()
        self.tb_alias.pack()
        header_fqdn.pack()
        self.tb_fqdn.pack()

        self.add_button.pack()
        
    def add_service(self, event=None):
        
        if self.tb_alias.get() is None:
            return
        
        self.database.services_add_service(self.tb_alias.get(), self.tb_fqdn.get())
        self.root.destroy()


class ServicesForm():

    def __init__(self, parent: tk.Frame):

        self.parent = parent
        self.database = database
        self.root = tk.Frame(self.parent)

        header_users = tk.Label(self.root, text="Список пользователей")
        self.header_user_services = tk.Label(self.root, text="*Нажмите на пользователя чтобы просмотреть сервисы.")

        self.users_list = tk.Listbox(self.root)
        self.user_services_list = tk.Listbox(self.root)
        self.update_users()
        self.users_list.bind('<<ListboxSelect>>', self.update_user_services)

        self.last_selected_user_id = None
        self.last_selected_user_service_id = None
        self.last_selected_service_id = None

        self.update_user_services()

        self.button_add_user_service = tk.Button(self.root, text="Добавить", command=self.add_user_service)
        self.button_del_user_service = tk.Button(self.root, text="Удалить", command=self.del_user_service)

        header_services = tk.Label(self.root, text="Список всех сервисов")
        self.services_list = tk.Listbox(self.root)
        self.update_services()
        self.services_list.bind('<<ListboxSelect>>', self.update_service_data)
        self.button_add_service = tk.Button(self.root, text="Добавить", command=self.add_service)
        self.button_del_service = tk.Button(self.root, text="Удалить", command=self.del_service)

        self.service_data = tk.Frame(self.root)
        header_alias = tk.Label(self.service_data, text="Псевдоним")
        self.tv_alias = tk.StringVar()
        self.service_data_alias = tk.Entry(self.service_data, textvariable=self.tv_alias)
        self.service_data_alias.bind('<Return>', self.update_service_alias)
        header_fqdn = tk.Label(self.service_data, text="FQDN")
        self.tv_fqdn = tk.StringVar()
        self.service_data_fqdn = tk.Entry(self.service_data, textvariable=self.tv_fqdn)
        self.service_data_fqdn.bind('<Return>', self.update_service_fqdn)
        help_label = tk.Label(self.service_data, text="*Нажмите Enter для изменения")

        header_users.grid(column=0, row=0)
        self.users_list.grid(column=0, row=1)
        self.header_user_services.grid(column=1, row=0)
        self.user_services_list.grid(column=1, row=1)
        self.button_add_user_service.grid(column=1, row=2)
        self.button_del_user_service.grid(column=1, row=3)

        header_services.grid(column=0, row=4)
        self.services_list.grid(column=0, row=5)
        self.button_add_service.grid(column=0, row=6)
        self.button_del_service.grid(column=0, row=7)
        
        header_alias.pack()
        self.service_data_alias.pack()
        header_fqdn.pack()
        self.service_data_fqdn.pack()
        help_label.pack()

        self.service_data.grid(column=1, row=5)

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

    def _get_selected_user_service_id(self):

        if not hasattr(self, "user_services_list"):
            return None

        selection = self.user_services_list.curselection()

        if len(selection) <= 0:
            return None

        service_alias = self.user_services_list.selection_get()

        if service_alias is None:
            return None

        service_id = database.services_get_by_alias(alias=service_alias)[0][0]
        self.last_selected_user_service_id = service_id

        return service_id
    
    def _get_selected_service_id(self):

        if not hasattr(self, "services_list"):
            return None

        selection = self.services_list.curselection()

        if len(selection) <= 0:
            return None

        service_index = int(selection[0])

        if service_index is None:
            return None
        if service_index < 0:
            return None

        service_id = database.services_get_all()[service_index][0]
        self.last_selected_service_id = service_id

        return service_id

    def update_users(self, event=None):

        if not hasattr(self, "services_list"):
            return
        
        self.users_list.delete(0, tk.END)
        
        users = database.users_get_all()
        for user in users:
            self.users_list.insert(tk.END, user[1])

    def update_user_services(self, event=None):
        
        user_id = self._get_selected_user_id()

        if user_id is None:
            
            if (user_id := self.last_selected_user_id) is None:

                return

        services = database.services_get_by_user(user_id)
        
        self.user_services_list.delete(0, tk.END)
        self.header_user_services.configure(text="Список сервисов пользователя")
        for service in services:
            self.user_services_list.insert(tk.END, service[1])

    def update_services(self, event=None):

        services = database.services_get_all()
        
        self.services_list.delete(0, tk.END)
        for service in services:
            self.services_list.insert(tk.END, service[1])

    def add_user_service(self, event=None):

        user_id = self._get_selected_user_id()

        if user_id is None:
            
            if (user_id := self.last_selected_user_id) is None:

                return

        add_user_service_form = AddUserServiceForm(self.root, user_id)
        add_user_service_form.root.bind("<Destroy>", self.update_user_services)

    def del_user_service(self, event=None):

        service_id = self._get_selected_user_service_id()

        if service_id is None:

            if (service_id := self.last_selected_user_service_id) is None:

                return
        
        user_id = self._get_selected_user_id()

        if user_id is None:

            if (user_id := self.last_selected_user_id) is None:

                return

        database.services_del_from_user(user_id, service_id)

        self.update_user_services()

    def add_service(self, event=None):

        add_service_form = AddServiceForm(self.root)
        add_service_form.root.bind("<Destroy>", self.update_services)

    def del_service(self, event=None):

        service_id = self._get_selected_service_id()
        if service_id is None:

            if (service_id := self.last_selected_service_id) is None:

                return

        database.services_delete_service(service_id)
        self.update_services()

    def update_service_data(self, event=None):

        service_id = self._get_selected_service_id()

        if service_id is None:

            if (service_id := self.last_selected_service_id) is None:

                return
            
        service = database.services_get_by_id(service_id)[0]
        
        self.service_data_alias.delete(0, tk.END)
        self.service_data_alias.insert(0, service[1])
        self.service_data_fqdn.delete(0, tk.END)
        self.service_data_fqdn.insert(0, service[2])

    def update_service_alias(self, event=None):

        service_id = self._get_selected_service_id()

        if service_id is None:

            if (service_id := self.last_selected_service_id) is None:

                return False

        if messagebox.askyesno("Внимание!", "Изменить псевдоним сервиса?"):
            
            database.services_update_service(service_id, alias=self.service_data_alias.get())
            self.update_services()
            return True

        return False

    def update_service_fqdn(self, event=None):

        service_id = self._get_selected_service_id()

        if service_id is None:

            if (service_id := self.last_selected_service_id) is None:

                return False

        if messagebox.askyesno("Внимание!", "Изменить FQDN (Доменное имя) устройства?"):
            database.services_update_service(service_id, fqdn=self.service_data_fqdn.get())
            self.update_services()
            return True

        return False
