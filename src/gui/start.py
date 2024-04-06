from src.gui.login_form import LoginWindow

def start(database):

    login_window = LoginWindow(database)
    login_window.parent.mainloop()