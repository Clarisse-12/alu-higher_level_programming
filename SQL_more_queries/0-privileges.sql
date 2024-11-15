
-- Script that lists all privileges of the MySQL users
-- Query to list all privileges (GRANT) of the MySQL uses
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

DELIMITER //

CREATE PROCEDURE RevokeAllPrivileges(IN username VARCHAR(100), IN host VARCHAR(100))
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE grant_statement TEXT;
    DECLARE cur CURSOR FOR SHOW GRANTS FOR username@host;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

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
END//

DELIMITER ;

CALL RevokeAllPrivileges('user_0d_1', 'localhost');
CALL RevokeAllPrivileges('user_0d_2', 'localhost');

DROP PROCEDURE IF EXISTS RevokeAllPrivileges;

