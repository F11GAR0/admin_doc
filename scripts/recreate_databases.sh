#!/bin/bash
/opt/RedDatabase/bin/isql -q -u sysdba -p masterkey < sql/drop_databases.sql
/opt/RedDatabase/bin/isql -q -u sysdba -p masterkey < sql/create_databases.sql
/opt/RedDatabase/bin/isql -q -u sysdba -p masterkey < sql/create_tables.sql
/opt/RedDatabase/bin/isql -q -u sysdba -p masterkey < sql/show_tables.sql
/opt/RedDatabase/bin/isql -q -u sysdba -p masterkey < sql/add_test_data.sql