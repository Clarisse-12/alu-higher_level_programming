
-- Script that lists all privileges of the MySQL users
-- Query to list all privileges (GRANT) of the MySQL uses
DELIMITER //

CREATE PROCEDURE RevokeAllPrivileges(IN username VARCHAR(100), IN host VARCHAR(100))
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE grant_statement TEXT;
    DECLARE cur CURSOR FOR SELECT grant_query FROM mysql.temp_grants;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    CREATE TEMPORARY TABLE IF NOT EXISTS mysql.temp_grants (grant_query TEXT);

    SET @show_grants_query = CONCAT("SHOW GRANTS FOR '", username, "'@'", host, "'");
    PREPARE stmt FROM @show_grants_query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    INSERT INTO mysql.temp_grants (grant_query)
    SELECT DISTINCT CONCAT('GRANT ', PRIVILEGE_TYPE, ' ON *.* TO ''', username, '''@''', host, '''')
    FROM information_schema.user_privileges
    WHERE GRANTEE = CONCAT("'", username, "'@", host);

    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO grant_statement;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SET @revoke_stmt = REPLACE(grant_statement, 'GRANT', 'REVOKE');
        SET @revoke_stmt = REPLACE(@revoke_stmt, 'TO', 'FROM');

        PREPARE stmt FROM @revoke_stmt;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;
    CLOSE cur;

    DROP TEMPORARY TABLE IF EXISTS mysql.temp_grants;
END//

DELIMITER ;

CALL RevokeAllPrivileges('user_0d_1', 'localhost');
CALL RevokeAllPrivileges('user_0d_2', 'localhost');

DROP PROCEDURE IF EXISTS RevokeAllPrivileges;

