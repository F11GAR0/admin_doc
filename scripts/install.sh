#!/bin/bash
mkdir /var/lib/rdb
mkdir /tmp/firebird
chown firebird:firebird -R /var/lib/rdb
chmod 777 -R /var/lib/rdb
chown firebird:firebird -R /tmp/firebird
chmod 777 -R /tmp/firebird
chmod +x scripts/*.sh
if grep -q 'admindoc' /opt/RedDatabase/databases.conf; then
	echo 'Config already configurated'
else
	echo 'admindoc = /var/lib/rdb/admindoc.fdb' >> /opt/RedDatabase/databases.conf
fi
sed -i 's/#RemoteBindAddress =/RemoteBindAddress = 127.0.0.1/' /opt/RedDatabase/firebird.conf
/opt/RedDatabase/bin/isql -q -u sysdba -p masterkey < sql/create_databases.sql
systemctl start firebird
/opt/RedDatabase/bin/isql -q -u sysdba -p masterkey < sql/create_tables.sql
/opt/RedDatabase/bin/isql -q -u sysdba -p masterkey < sql/add_test_data.sql