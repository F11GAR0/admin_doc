import firebird.driver as driver

class Database:

    def __init__(self):

        self.connection = driver.connect('admindoc', user='sysdba', password='masterkey')
        self.cursor = self.connection.cursor()
    
    def __del__(self):

        if self.connection:
            self.connection.close()

    def users_passwd_get_by_id(self, id_user):

        self.cursor.execute(f"select password_hash from users where id_user={id_user}")
        return self.cursor.fetchall()[0][0]

    def users_get_id_by_email(self, email):

        self.cursor.execute(f"select id_user from users where email={email}")
        return self.cursor.fetchall()[0][0]

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








