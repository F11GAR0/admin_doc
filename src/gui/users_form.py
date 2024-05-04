import tkinter as tk
import tksheet

from src.lib.rdb.model import AuthError, database, auth

class AddUserForm():

    def __init__(self, parent):

        self.root = tk.Toplevel(parent)
        self.frame = tk.Frame(self.root)
        email_label = tk.Label(self.frame, text="Email: ")
        self.email_textbox = tk.Entry(self.frame)
        password_label = tk.Label(self.frame, text="Пароль: ")
        self.password_textbox = tk.Entry(self.frame, show="*")
        first_name_label = tk.Label(self.frame, text="Имя: ")
        self.first_name_textbox = tk.Entry(self.frame)
        last_name_label = tk.Label(self.frame, text="Фамилия: ")
        self.last_name_textbox = tk.Entry(self.frame)
        self.button_add_user = tk.Button(self.frame, text="Добавить", command=self.add_user)

        self.message = tk.StringVar(self.frame)
        self.message_label = tk.Label(self.frame, textvariable=self.message)

        email_label.grid(column=0, row=0)
        self.email_textbox.grid(column=1, row=0)
        password_label.grid(column=0, row=1)
        self.password_textbox.grid(column=1, row=1)
        first_name_label.grid(column=0, row=2)
        self.first_name_textbox.grid(column=1, row=2)
        last_name_label.grid(column=0, row=3)
        self.last_name_textbox.grid(column=1,row=3)
        self.button_add_user.grid(column=0, row=4)
        self.message_label.grid(column=0, row=5)

        self.frame.place(in_=self.root, anchor="c", relx=.5, rely=.5)

    def add_user(self):

        try:
            auth.add_user(self.email_textbox.get(),
                        self.password_textbox.get(),
                        self.first_name_textbox.get(),
                        self.last_name_textbox.get())
            self.root.destroy()
        except AuthError as e:
            self.message.set(str(e))


class UsersForm():

    def __init__(self, parent):

        self.parent = parent
        self.database = database
        self.root = tk.Frame(self.parent, background="gray", padx=5, pady=15)

        self.table = tksheet.Sheet(self.root, "Список пользователей")
        self.table.headers("Initial", 4)
        self.table.headers()[0] = "Идентификатор"
        self.table.headers()[1] = "Email"
        self.table.headers()[2] = "Хэш пароля"
        self.table.headers()[3] = "Имя"
        self.table.headers()[4] = "Фамилия"

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
        self.update_data()

    def delete_user(self):

        row = self.table.get_currently_selected().row
        user_id = self.table.get_cell_data(row, 0)
        database.users_delete_user(user_id)
        self.update_data()

    def add_user(self):

        add_user = AddUserForm(self.root)
        add_user.root.bind("<Destroy>", self.update_data)

    def update_data(self, event=None):

        self.table.set_sheet_data(data=database.users_get_all())
