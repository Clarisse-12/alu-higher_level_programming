-- Script that lists all privileges of the MySQL users
-- Query to list all privileges (GRANT) of the MySQL users
SELECT 
    GRANTEE, PRIVILEGE_TYPE, IS_GRANTABLE 
FROM 
    INFORMATION_SCHEMA.USER_PRIVILEGES
WHERE 
    GRANTEE IN ('\'user_0d_1\'@\'localhost\'', '\'user_0d_2\'@\'localhost\'');
