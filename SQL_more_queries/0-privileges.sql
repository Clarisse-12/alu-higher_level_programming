-- Script that lists all privileges of the MySQL users
-- Query to list all privileges (GRANT) of the MySQL users
import mysql.connector

def list_user_privileges(users):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password'
        )
        
        cursor = connection.cursor()
        
        for user in users:
            cursor.execute(f"SHOW GRANTS FOR '{user}'@'localhost';")
            grants = cursor.fetchall()
            print(f"Privileges for {user}:")
            for grant in grants:
                print(grant[0])
            print("\n")
            
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

users_to_check = ['user_0d_1', 'user_0d_2']
list_user_privileges(users_to_check)
