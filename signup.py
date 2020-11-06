#!C:\python 3.8\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector

try:
    db=mysql.connector.connect(host="127.0.0.1",user="root",password="",db="college")
    cursor=db.cursor()
    data=cgi.FieldStorage()
    name=data.getvalue('name')
    roll=int(data.getvalue('roll'))
    email=data.getvalue('email')
    password=data.getvalue('password')
    stream=data.getvalue('stream')
    code=data.getvalue('C-code')
    if code=='ariyo2007':

        sql_query="insert into students values('%s', '%s', '%s', '%s', '%d')"%(name, email, stream, password, roll)
        cursor.execute(sql_query)
        db.commit()
        print("""
        <link rel="stylesheet" type="text/css" href="style.css">
        <h1 class='center'>You are successfully Registered Up <a style='text-decoration:none;' href='main.py'> Click Here</a></h1>
        """)
    else: 
        print("""<link rel="stylesheet" type="text/css" href="style.css">
        <h1 class='center'>Wrong code</h1>""")
except Exception as e:
    print(e)

