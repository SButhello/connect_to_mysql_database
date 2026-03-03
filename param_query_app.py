import mysql.connector as mydbconnection
from mysql.connector import Error

def get_laptop_detail(id):
    conn = mydbconnection.connect(database='classicmodels', user='root', password='root')
    cursor = conn.cursor()
    sql_select_query = """select * from offices where officeCode = %s"""
    # set variable in query
    cursor.execute(sql_select_query, (id,))
    # fetch result
    record = cursor.fetchall()

    for row in record:
        print("officeCode = ", row[0], )
        print("city = ", row[1])
        print("Phone = ", row[2])
        print("addressline1  = ", row[3], "\n")
        cursor.close()
        conn.close()
        print("MySQL connection is closed")

get_laptop_detail(1)
get_laptop_detail(2)
