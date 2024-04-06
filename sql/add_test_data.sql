connect 'admindoc' user sysdba password 'masterkey';

insert into users (email, password_hash, first_name, last_name)
    values ('alexandr.lushin@red-soft.ru' , '5f4dcc3b5aa765d61d8327deb882cf99', 'Alexander', 'Lushin');
commit;

insert into devices (alias, ipv4, ipv6, fqdn) 
    values ('Alexandr Lushin PC', '10.100.1.53', '', 'lushin-dev-pc.some.dev');
commit;

insert into external_users (id_user, email, password_hash)
    values (1, 'drevojizni@hhru.anonaddy.me', '5f4dcc3b5aa765d61d8327deb882cf99');
commit;

insert into user_devices (id_user, id_device)
    values (1,1);
commit;

insert into roles (alias, role_content)
    values ('SuperUser', '{ "is_superuser" : true }');
insert into roles (alias, role_content)
    values ('Guest', '{ "is_guest" : true }');
insert into roles (alias, role_content)
    values ('SystemAdministrator', '{ "is_sysadmin" : true }');
commit;

insert into user_permissions (id_user, id_role)
    values (1,1);
commit;

insert into services (alias, fqdn)
    values ('Corporative eMail', 'mail.some.dev');
commit;

insert into user_services (id_user, id_service)
    values (1, 1);
commit;