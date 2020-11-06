#!C:\python 3.8\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
try:
    db=mysql.connector.connect(host="127.0.0.1",user="root",password="",db="college")
    cursor=db.cursor()
    data=cgi.FieldStorage()
    email=data.getvalue('email')
    password=data.getvalue('password')
    
    sql_query="select * from students where email='%s' and password='%s'"%(email, password)
    cursor.execute(sql_query)
    result=cursor.fetchone()
    db.commit()
    name=data.getvalue('name')
    if result!=None:
        print(f"""<link rel="stylesheet" type="text/css" href="style.css">
        <h1 class='center'>You are successfully LoggedIn <a href='main.py/?name={name}'> Click Here</a></h1>""")
    else:
        print("""<link rel="stylesheet" type="text/css" href="style.css">
        <h1 class='center' style='color:red;'>Wrong Details!!!!!</h1>""")
    db.close()
    cursor.close()
except Exception as e:
    print(e)
