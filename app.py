import mysql.connector as dbconnection
from mysql.connector import Error


myconnection = None
cursor = None

try:
    # Create connection to mysql
    myconnection = dbconnection.connect(host='localhost', database='classicmodels', user='root', password='root')
    if myconnection.is_connected():
        print('Successfully Connected to MySQL database')
        cursor = myconnection.cursor()
        SQLQuery ="SELECT ordernumber, SUM(quantityOrdered) AS itemsCount, SUM(priceeach*quantityOrdered) AS total FROM orderdetails GROUP BY ordernumber HAVING    total > 1000    AND    itemsCount > 600";
        cursor.execute(SQLQuery)
        # get all records
        records = cursor.fetchall()   
        print("Total number of rows in table: ", cursor.rowcount)    
        print("\nPrinting each row")
        for row in records:
            print("order number = ", row[0],  )
            print("item counts = ", row[1])
            print("total  = ", row[2], "\n" )
except Error as e:
        print("Error while connecting to Database", e)
finally:
        if myconnection is not None and myconnection.is_connected():
            if cursor is not None:
                cursor.close()
            myconnection.close()
        print("Database connection is closed")