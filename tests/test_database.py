import pytest
from firebird import driver


class TestDatabase:

    @staticmethod
    def connect_and_execute(query):

        with driver.connect('admindoc', user='sysdba', password='masterkey') as con:

            cur = con.cursor()
            cur.execute(query)
            ret = cur.fetchall()

            return ret

    @pytest.mark.xfail
    def test_clean_database(self):

        result_devices = TestDatabase.connect_and_execute('select * from devices')
        result_users = TestDatabase.connect_and_execute('select * from users')
        result_external_users = TestDatabase.connect_and_execute('select * from external_users')
        result_user_devices = TestDatabase.connect_and_execute('select * from user_devices')
        result_roles = TestDatabase.connect_and_execute('select * from roles')
        result_user_permissions = TestDatabase.connect_and_execute('select * from user_permissions')
        result_services = TestDatabase.connect_and_execute('select * from services')
        result_user_services = TestDatabase.connect_and_execute('select * from user_services')

        assert len(result_devices) == 0
        assert len(result_users) == 0
        assert len(result_external_users) == 0
        assert len(result_user_devices) == 0
        assert len(result_roles) == 0
        assert len(result_user_permissions) == 0
        assert len(result_services) == 0
        assert len(result_user_services) == 0
