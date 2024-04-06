import firebird.driver as driver
from src.lib.crypt.hash import validate_password

class Database:

    def __init__(self):

        self.connection = driver.connect('admindoc', user='sysdba', password='masterkey')
        self.cursor = self.connection.cursor()
    
    def __del__(self):

        if self.connection:
            self.connection.close()

    def users_passwd_get_by_id(self, id_user):

        self.cursor.execute(f"select password_hash from users where id_user={id_user}")
        return self.cursor.fetchone()[0]

    def users_get_id_by_email(self, email):

        self.cursor.execute(f"select id_user from users where email='{email}'")
        
        try:
            return self.cursor.fetchone()[0]
        except driver.types.DatabaseError as _:
            return None
        
    def users_get_all(self):

        self.cursor.execute("select * from users")
        return self.cursor.fetchall()

    def users_get_by_id(self, id_user):
        
        self.cursor.execute(f"select * from users where id_user={id_user}")
        return self.cursor.fetchall()

    def devices_get_all(self):

        self.cursor.execute("select * from devices")
        return self.cursor.fetchall()

    def devices_get_by_id(self, id_device):

        self.cursor.execute(f"select * from devices where id_device={id_device}")
        return self.cursor.fetchall()

    def roles_get_all(self):

        self.cursor.execute("select * from roles")
        return self.cursor.fetchall()

    def services_get_all(self):

        self.cursor.execute("select * from services")
        return self.cursor.fetchall()

    def external_users_get_all(self):

        self.cursor.execute("select * from external_users")
        return self.cursor.fetchall()

    # Many to Many

    def user_devices_get_all(self):

        self.cursor.execute("select * from user_devices")
        return self.cursor.fetchall()

    def user_permissions_get_all(self):

        self.cursor.execute("select * from user_permissions")
        return self.cursor.fetchall()

    def user_services_get_all(self):

        self.cursor.execute("select * from user_services")
        return self.cursor.fetchall()

database = Database()

class AuthError(Exception):

    pass

class Auth(object):

    def __init__(self):

        pass

    def __validate_login_mock(self, login, password):

        return True
    
    def __validate_login(self, login,password):

        if len(login) <= 0:
            raise AuthError("Please, enter email.")
        
        if len(password) <= 0:
            raise AuthError("Please, enter password.")

        user_id = database.users_get_id_by_email(login)

        if user_id is None:
            raise AuthError("Wrong email or password. Try again.")

        user_password_hash = database.users_passwd_get_by_id(user_id)

        if validate_password(password, user_password_hash):
            return True
        else:
            raise AuthError("Wrong email or password. Try again.")

    def validate_login(self, login, password):

        return self.__validate_login_mock(login, password)

auth = Auth()   



