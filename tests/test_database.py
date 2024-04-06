import pytest
import firebird.driver as driver
from src.lib.rdb.model import AdminDocumentation


class TestDatabase:

    def __init__(self):

        pass

    def connect_and_execute(query):

        con = driver.connect('admindoc', user='sysdba', password='masterkey')

        cur = con.cursor()

        cur.execute(query)

        return cur.fetchall()


    def test_clean_database(self):

        result_devices = connect_and_execute('select * from devices')
        result_users = connect_and_execute('select * from users')
        result_external_users = connect_and_execute('select * from external_users')
        result_user_devices = connect_and_execute('select * from user_devices')
        result_roles = connect_and_execute('select * from roles')
        result_user_permissions = connect_and_execute('select * from user_permissions')
        result_services = connect_and_execute('select * from services')
        result_user_services = connect_and_execute('select * from user_services')

        assert len(result_devices) == 0
        assert len(result_users) == 0
        assert len(result_external_users) == 0
        assert len(result_user_devices) == 0
        assert len(result_roles) == 0
        assert len(result_user_permissions) == 0
        assert len(result_services) == 0
        assert len(result_user_services) == 0

    def test_add_role(self):

        db = AdminDocumentation()
        result = db.add_role(alias='Testing role', role_content='01010101110101')
        print(result)

