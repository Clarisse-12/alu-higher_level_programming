
-- Script that lists all privileges of the MySQL users;
SELECT USER, HOST FROM mysql.user
WHERE USER IN ('user_0d_1', 'user_0d_2')
AND HOST = 'localhost';

SHOW GRANTS FOR 'user_0d_1'@'localhost';

SHOW GRANTS FOR 'user_0d_2'@'localhost';

SELECT DISTINCT
   GRANTEE,
   TABLE_SCHEMA,
   TABLE_NAME,
   PRIVILEGE_TYPE
FROM information_schema.TABLE_PRIVILEGES
WHERE GRANTEE IN (
   "'user_0d_1'@'localhost'",
   "'user_0d_2'@'localhost'"
)
ORDER BY GRANTEE, TABLE_SCHEMA, TABLE_NAME, PRIVILEGE_TYPE;

SELECT
   USER,
   HOST,
   SELECT_PRIV,
   INSERT_PRIV,
   UPDATE_PRIV,
   DELETE_PRIV,
   CREATE_PRIV,
   DROP_PRIV,
   RELOAD_PRIV,
   SHUTDOWN_PRIV,
   PROCESS_PRIV,
   FILE_PRIV,
   GRANT_PRIV,
   REFERENCES_PRIV,
   INDEX_PRIV,
   ALTER_PRIV,
   SHOW_DB_PRIV,
   SUPER_PRIV,
   CREATE_TMP_TABLE_PRIV,
   LOCK_TABLES_PRIV,
   EXECUTE_PRIV,
   REPL_SLAVE_PRIV,
   REPL_CLIENT_PRIV
FROM mysql.user
WHERE USER IN ('user_0d_1', 'user_0d_2')
AND HOST = 'localhost';
