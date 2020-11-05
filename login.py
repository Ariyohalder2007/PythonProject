#!C:\python 3.8\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
db=mysql.connector.connect(host="127.0.0.1",user="root",password="",db="ecomsite")
cursor=db.cursor()
data=cgi.FieldStorage()
email=data.getvalue('email')
password=data.getvalue('password')
sql_query="select * from customers where email='%s' and password='%s'"%(email, password)
cursor.execute(sql_query)
result=cursor.fetchone()
db.commit()
if result!=None:
    print("""<link rel="stylesheet" type="text/css" href="style.css">
    <h1 class='center'>You are successfully LoggedIn <a href='main.py'> Click Here</a></h1>""")
else:
    print("""<link rel="stylesheet" type="text/css" href="style.css">
    <h1 class='center' style='color:red;'>Wrong Details!!!!!</h1>""")
db.close()
cursor.close()