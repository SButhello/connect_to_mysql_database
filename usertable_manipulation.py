

#--------------------------------------------------------------------
              #Create Table
#-------------------------------------------------------------------


import mysql.connector as mydbconnection
from mysql.connector import Error
try:
	conn = mydbconnection.connect(database='registrationdb1', user='root',password='root', port ='3306')
	cursor=conn.cursor()
	myquery2 = "CREATE TABLE `usertable_manipulation` (`email` varchar(100) NOT NULL,\
  `Name` varchar(50) NOT NULL,\
  `password` varchar(30) NOT NULL)"
	cursor.execute(myquery2)
	print("Table is created")
except Error as e:
    print("Failed tocreate table {}".format(e))
finally:
   if conn.is_connected():
    conn.close()
    print("MySQL connection is closed")

#------------------------------------------------------------------------------
                              #Insert Into table 
#-----------------------------------------------------------------------------------


import mysql.connector as mydbconnection
from mysql.connector import Error
def insert_varibles_into_table(email, name, password):
    try:
        conn = mydbconnection.connect(database='registrationdb1', user='root',password='root', port ='3306')
        cursor = conn.cursor()
        mySql_insert_query = """INSERT INTO usertable_manipulation (email, name, password)VALUES (%s, %s, %s) """                  

        record = (email, name, password)
        cursor.execute(mySql_insert_query, record)
        conn.commit()
        print("Record inserted successfully into usertable_manipulation table")

    except Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")


insert_varibles_into_table( 'ywbaek@perscholas.org', 'young', 'letsgomets')
insert_varibles_into_table( 'mcordon@perscholas.org', 'marcial', 'perscholas')
insert_varibles_into_table(  'mhaseeb@perscholas.org', 'haseeb', 'platform')

#-----------------------------------------------------------------------
                       #get_all_users() Method
#------------------------------------------------------------------------


import mysql.connector as mydbconnection
from mysql.connector import Error

def get_all_users():
    try:
        conn = mydbconnection.connect(
            database='registrationdb1',
            user='root',
            password='root',
            port='3306'
        )

        if conn.is_connected():
            cursor = conn.cursor()

            query = "SELECT email, name, password FROM usertable_manipulation"
            cursor.execute(query)

            records = cursor.fetchall()

            print("All Users:")
            print("----------------------------")

            for row in records:
                print("Email:", row[0])
                print("Name:", row[1])
                print("Password:", row[2])
                print("----------------------------")

    except Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")

get_all_users()

#-------------------------------------------------------------------------
                  #get_user_by_name(name) Method
#-------------------------------------------------------------------------


import mysql.connector as mydbconnection
from mysql.connector import Error

def get_user_by_name(name):
    try:
        conn = mydbconnection.connect(
            database='registrationdb1',
            user='root',
            password='root',
            port='3306'
        )

        if conn.is_connected():
            cursor = conn.cursor()

            query = "SELECT email, password FROM usertable_manipulation WHERE name = %s"
            cursor.execute(query, (name,))

            records = cursor.fetchall()

            if records:
                print("User Details:")
                print("---------------------")
                for row in records:
                    print("Email:", row[0])
                    print("Password:", row[1])
            else:
                print("No user found with the name:", name)

    except Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")



get_user_by_name("young")

#-------------------------------------------------------------------------
             #validate_user(email, password) Method:
#-------------------------------------------------------------------------

import mysql.connector as mydbconnection
from mysql.connector import Error

def validate_user(email, password):
    try:
        conn = mydbconnection.connect(
            host="localhost",
            database="registrationdb1",
            user="root",
            password="root",
            port="3306"
        )

        cursor = conn.cursor()

        query = "SELECT * FROM usertable_manipulation WHERE email=%s AND password=%s"
        cursor.execute(query, (email, password))

        record = cursor.fetchone()

        if record:
            return True
        else:
            return False

    except Error as e:
        print("Error:", e)
        return False

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


# Calling the function
result = validate_user("ywbaek@perscholas.org", "letsgomets")

if result:
    print("User is valid")
else:
    print("Invalid email or password")

#--------------------------------------------------------------------------
            #update_user(email, name, password) method:
#--------------------------------------------------------------------------

import mysql.connector as mydbconnection
from mysql.connector import Error

def update_user(email, name, password):
    try:
        conn = mydbconnection.connect(
            host="localhost",
            database="registrationdb1",
            user="root",
            password="root",
            port="3306"
        )

        if conn.is_connected():
            cursor = conn.cursor()

            query = """UPDATE usertable_manipulation
                       SET name=%s, password=%s
                       WHERE email=%s"""

            cursor.execute(query, (name, password, email))
            conn.commit()

            if cursor.rowcount > 0:
                return True
            else:
                return False

    except Error as e:
        print("Error:", e)
        return False

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


# Test the function with your values
result = update_user('ywbaek@perscholas.org', 'young kim', 'letsgometss')

if result:
    print("User updated successfully")
else:
    print("User not found or update failed")
