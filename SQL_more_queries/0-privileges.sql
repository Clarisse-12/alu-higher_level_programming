
-- Script that lists all privileges of the MySQL users
-- Query to list all privileges (GRANT) of the MySQL users
REVOKE SELECT, INSERT, UPDATE ON *.* FROM 'user_0d_1'@'localhost';
REVOKE CREATE, DROP ON db1.* FROM 'user_0d_1'@'localhost';

