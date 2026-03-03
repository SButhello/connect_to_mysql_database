import mysql.connector as mydbconnection
from mysql.connector import Error

conn = mydbconnection.connect(database='classicmodels', user='root',password='root', port ='3306')

cursor=conn.cursor()

myquery = "CREATE TABLE tasks (task_id INT AUTO_INCREMENT,title VARCHAR(255) NOT NULL,\
start_date DATE,\
due_date DATE,\
priority TINYINT NOT NULL DEFAULT 3,\
description TEXT,\
PRIMARY KEY (task_id))"

print(myquery)

cursor.execute(myquery)
cursor.close
conn.close()