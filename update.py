#!C:\python 3.8\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector

db=mysql.connector.connect(host="127.0.0.1",user="root",password="",db="college")
cursor=db.cursor()
data=cgi.FieldStorage()
name=data.getvalue("name")
roll=int(data.getvalue("roll"))
stream=data.getvalue("stream")
email=data.getvalue("email")
password=data.getvalue("password")
sql="update students set name='%s',email='%s',password='%s',stream='%s' where roll=%d"%(name,email,password,stream,roll)
#delete from student where roll=%d and email='%s'
cursor.execute(sql)
db.commit()
nav=open('nav.html', 'r')
print(f"""

<link rel="stylesheet" href="/college/style.css">
{nav.read()}
<h2 class="center" style="color: green; margin: 30px;"> Updated Successfully Now You Can Go to 


<a href="/college/main.py?name={name}">DashBoard</a>
 </h2>
<script src="https://kit.fontawesome.com/2f47edd958.js" crossorigin="anonymous"></script>
""")
nav.close()
db.close()
cursor.close()