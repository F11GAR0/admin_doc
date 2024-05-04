import tkinter as tk 
from tkinter import messagebox

from src.lib.rdb.model import database


class AddUserDeviceForm():

    def __init__(self, parent, user_id):

        self.parent = parent
        self.database = database
        self.user_id = user_id
        self.root = tk.Toplevel(self.parent)

        header_devices = tk.Label(self.root, text="Список существующих устройств")
        self.devices_list = tk.Listbox(self.root)
        self.update_devices()
        self.add_button = tk.Button(self.root, text="Добавить", command=self.add_device)

        header_devices.pack()
        self.devices_list.pack()
        self.add_button.pack()

    def update_devices(self, event=None):

        if not hasattr(self, "devices_list"):
            return

        roles = database.devices_get_all()
        
        self.devices_list.delete(0, tk.END)
        
        for role in roles:
            self.devices_list.insert(tk.END, role[1])

    def add_device(self, event=None):

        selection = self.devices_list.curselection()

        if len(selection) <= 0:
            return

        device_index = int(selection[0])

        if device_index is None:
            return
        if device_index < 0:
            return

        device_id = database.devices_get_all()[device_index][0]
        database.devices_add_to_user(self.user_id, device_id)
        self.root.destroy()


class AddDeviceForm():

    def __init__(self, parent):

        self.parent = parent
        self.database = database
        self.root = tk.Toplevel(self.parent)

        header_alias = tk.Label(self.root, text="Псевдоним")
        self.tb_alias = tk.Entry(self.root)
        header_ipv4 = tk.Label(self.root, text="IPv4")
        self.tb_ipv4 = tk.Entry(self.root)
        header_ipv6 = tk.Label(self.root, text="IPv6")
        self.tb_ipv6 = tk.Entry(self.root)
        header_fqdn = tk.Label(self.root, text="FQDN (Domain name)")
        self.tb_fqdn = tk.Entry(self.root)

        self.add_button = tk.Button(self.root, text="Добавить", command=self.add_device)

        header_alias.pack()
        self.tb_alias.pack()
        header_ipv4.pack()
        self.tb_ipv4.pack()
        header_ipv6.pack()
        self.tb_ipv6.pack()
        header_fqdn.pack()
        self.tb_fqdn.pack()

        self.add_button.pack()
        
    def add_device(self, event=None):
        
        if self.tb_alias.get() is None:
            return
        
        self.database.devices_add_device(self.tb_alias.get(), self.tb_ipv4.get(), self.tb_ipv6.get(), self.tb_fqdn.get())
        self.root.destroy()


class DevicesForm():

    def __init__(self, parent: tk.Frame):

        self.parent = parent
        self.database = database
        self.root = tk.Frame(self.parent)

        header_users = tk.Label(self.root, text="Список пользователей")
        self.header_user_devices = tk.Label(self.root, text="*Нажмите на пользователя чтобы просмотреть устройства.")

        self.users_list = tk.Listbox(self.root)
        self.user_devices_list = tk.Listbox(self.root)
        self.update_users()
        self.users_list.bind('<<ListboxSelect>>', self.update_user_devices)

        self.last_selected_user_id = None
        self.last_selected_user_device_id = None
        self.last_selected_device_id = None

        self.update_user_devices()

        self.button_add_user_device = tk.Button(self.root, text="Добавить", command=self.add_user_device)
        self.button_del_user_device = tk.Button(self.root, text="Удалить", command=self.del_user_device)

        header_devices = tk.Label(self.root, text="Список всех устройств")
        self.devices_list = tk.Listbox(self.root)
        self.update_devices()
        self.devices_list.bind('<<ListboxSelect>>', self.update_device_data)
        self.button_add_device = tk.Button(self.root, text="Добавить", command=self.add_device)
        self.button_del_device = tk.Button(self.root, text="Удалить", command=self.del_device)

        self.device_data = tk.Frame(self.root)
        header_alias = tk.Label(self.device_data, text="Псевдоним")
        self.tv_alias = tk.StringVar()
        self.device_data_alias = tk.Entry(self.device_data, textvariable=self.tv_alias)
        self.device_data_alias.bind('<Return>', self.update_device_alias)
        header_ipv4 = tk.Label(self.device_data, text="IPv4")
        self.tv_ipv4 = tk.StringVar()
        self.device_data_ipv4 = tk.Entry(self.device_data, textvariable=self.tv_ipv4)
        self.device_data_ipv4.bind('<Return>', self.update_device_ipv4)
        header_ipv6 = tk.Label(self.device_data, text="IPv6")
        self.tv_ipv6 = tk.StringVar()
        self.device_data_ipv6 = tk.Entry(self.device_data, textvariable=self.tv_ipv6)
        self.device_data_ipv6.bind('<Return>', self.update_device_ipv6)
        header_fqdn = tk.Label(self.device_data, text="FQDN (Domain name)")
        self.tv_fqdn = tk.StringVar()
        self.device_data_fqdn = tk.Entry(self.device_data, textvariable=self.tv_fqdn)
        self.device_data_fqdn.bind('<Return>', self.update_device_fqdn)
        help_label = tk.Label(self.device_data, text="*Нажмите Enter для изменения")

        header_users.grid(column=0, row=0)
        self.users_list.grid(column=0, row=1)
        self.header_user_devices.grid(column=1, row=0)
        self.user_devices_list.grid(column=1, row=1)
        self.button_add_user_device.grid(column=1, row=2)
        self.button_del_user_device.grid(column=1, row=3)

        header_devices.grid(column=0, row=4)
        self.devices_list.grid(column=0, row=5)
        self.button_add_device.grid(column=0, row=6)
        self.button_del_device.grid(column=0, row=7)
        
        header_alias.pack()
        self.device_data_alias.pack()
        header_ipv4.pack()
        self.device_data_ipv4.pack()
        header_ipv6.pack()
        self.device_data_ipv6.pack()
        header_fqdn.pack()
        self.device_data_fqdn.pack()
        help_label.pack()

        self.device_data.grid(column=1, row=5)

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

    def _get_selected_user_device_id(self):

        if not hasattr(self, "user_devices_list"):
            return None

        selection = self.user_devices_list.curselection()

        if len(selection) <= 0:
            return None

        device_alias = self.user_devices_list.selection_get()

        if device_alias is None:
            return None

        device_id = database.devices_get_by_alias(alias=device_alias)[0][0]
        self.last_selected_user_device_id = device_id

        return device_id
    
    def _get_selected_device_id(self):

        if not hasattr(self, "devices_list"):
            return None

        selection = self.devices_list.curselection()

        if len(selection) <= 0:
            return None

        device_index = int(selection[0])

        if device_index is None:
            return None
        if device_index < 0:
            return None

        device_id = database.devices_get_all()[device_index][0]
        self.last_selected_device_id = device_id

        return device_id

    def update_users(self, event=None):

        if not hasattr(self, "devices_list"):
            return
        
        self.users_list.delete(0, tk.END)
        
        users = database.users_get_all()
        for user in users:
            self.users_list.insert(tk.END, user[1])

    def update_user_devices(self, event=None):
        
        user_id = self._get_selected_user_id()

        if user_id is None:
            
            if (user_id := self.last_selected_user_id) is None:

                return

        devices = database.devices_get_by_user(user_id)
        
        self.user_devices_list.delete(0, tk.END)
        self.header_user_devices.configure(text="Список устройств пользователя")
        for device in devices:
            self.user_devices_list.insert(tk.END, device[1])

    def update_devices(self, event=None):

        devices = database.devices_get_all()
        
        self.devices_list.delete(0, tk.END)
        for device in devices:
            self.devices_list.insert(tk.END, device[1])

    def add_user_device(self, event=None):

        user_id = self._get_selected_user_id()

        if user_id is None:
            
            if (user_id := self.last_selected_user_id) is None:

                return

        add_user_device_form = AddUserDeviceForm(self.root, user_id)
        add_user_device_form.root.bind("<Destroy>", self.update_user_devices)

    def del_user_device(self, event=None):

        device_id = self._get_selected_user_device_id()

        if device_id is None:

            if (device_id := self.last_selected_user_device_id) is None:

                return
        
        user_id = self._get_selected_user_id()

        if user_id is None:

            if (user_id := self.last_selected_user_id) is None:

                return

        database.devices_del_from_user(user_id, device_id)

        self.update_user_devices()

    def add_device(self, event=None):

        add_device_form = AddDeviceForm(self.root)
        add_device_form.root.bind("<Destroy>", self.update_devices)

    def del_device(self, event=None):

        device_id = self._get_selected_device_id()
        if device_id is None:

            if (device_id := self.last_selected_device_id) is None:

                return

        database.devices_delele_device(device_id)
        self.update_devices()

    def update_device_data(self, event=None):

        device_id = self._get_selected_device_id()

        if device_id is None:

            if (device_id := self.last_selected_device_id) is None:

                return
            
        device = database.devices_get_by_id(device_id)[0]
        
        self.device_data_alias.delete(0, tk.END)
        self.device_data_alias.insert(0, device[1])
        self.device_data_ipv4.delete(0, tk.END)
        self.device_data_ipv4.insert(0, device[2])
        self.device_data_ipv6.delete(0, tk.END)
        self.device_data_ipv6.insert(0, device[3])
        self.device_data_fqdn.delete(0, tk.END)
        self.device_data_fqdn.insert(0, device[4])

    def update_device_alias(self, event=None):

        device_id = self._get_selected_device_id()

        if device_id is None:

            if (device_id := self.last_selected_device_id) is None:

                return False

        if messagebox.askyesno("Внимание!", "Изменить псевдоним устройства?"):
            
            database.devices_update_device(device_id, alias=self.device_data_alias.get())
            self.update_devices()
            return True

        return False

    def update_device_ipv4(self, event=None):

        device_id = self._get_selected_device_id()

        if device_id is None:

            if (device_id := self.last_selected_device_id) is None:

                return False

        if messagebox.askyesno("Внимание!", "Изменить IPv4 адрес устройства?"):

            database.devices_update_device(device_id, ipv4=self.device_data_ipv4.get())
            self.update_devices()
            return True

        return False

    def update_device_ipv6(self, event=None):

        device_id = self._get_selected_device_id()

        if device_id is None:

            if (device_id := self.last_selected_device_id) is None:

                return False

        if messagebox.askyesno("Внимание!", "Изменить IPv6 адрес устройства?"):

            database.devices_update_device(device_id, ipv6=self.device_data_ipv6.get())
            self.update_devices()
            return True

        return False

    def update_device_fqdn(self, event=None):

        device_id = self._get_selected_device_id()

        if device_id is None:

            if (device_id := self.last_selected_device_id) is None:

                return False

        if messagebox.askyesno("Внимание!", "Изменить FQDN (Доменное имя) устройства?"):
            database.devices_update_device(device_id, fqdn=self.device_data_fqdn.get())
            self.update_devices()
            return True

        return False
