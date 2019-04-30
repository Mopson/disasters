import mysql.connector

mydb = mysql.connector.connect(user='root', password='password', host='localhost', database='new_schema')

myCursor = mydb.cursor()

myCursor.execute("SELECT * FROM tornados_by_state")
myresult = myCursor.fetchall()

for x in myresult:
    print(x)