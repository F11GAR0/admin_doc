connect 'admindoc' user sysdba password 'masterkey';

delete from user_permissions where id_permission > 0;
delete from user_services where id_user_services > 0;
delete from user_devices where id_user_devices > 0;
delete from external_users where id_user_external > 0;
delete from roles where id_role > 0;
delete from users where id_user > 0;
delete from devices where id_device > 0;
delete from services where id_service > 0;
commit;
