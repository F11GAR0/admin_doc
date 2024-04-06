connect 'admindoc' user sysdba password 'masterkey';
select 
    RDB$FIELD_NAME AS "COLUMN", 
    RDB$RELATION_NAME AS "TABLE" 
from 
    rdb$relation_fields;
