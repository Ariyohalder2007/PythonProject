#!C:\python 3.8\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector

try:
    db=mysql.connector.connect(host="127.0.0.1",user="root",password="",db="ecomsite")
    cursor=db.cursor()
    data=cgi.FieldStorage()
    name=data.getvalue('name')
    phone=int(data.getvalue('phone'))
    email=data.getvalue('email')
    password=data.getvalue('password')

    sql_query="insert into customers values('%s', '%s', '%s', '%d')"%(name, email, password, phone)
    cursor.execute(sql_query)
    db.commit()
    print("""
    <link rel="stylesheet" type="text/css" href="style.css">
    <h1 class='center'>You are successfully Signed Up <a href='main.py'> Click Here</a></h1>
    """)
except Exception as e:
    print(e)

