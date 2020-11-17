#!C:\python 3.8\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
db=mysql.connector.connect(host="127.0.0.1",user="root",password="",db="college")
cursor=db.cursor()
data=cgi.FieldStorage()
roll=int(data.getvalue('roll'))
sql_query="select * from students where roll='%d'"%(roll)
cursor.execute(sql_query)
result=cursor.fetchone()
db.commit()
# print(result)
print(f"""
<h1> Welcome {result[0]}</h1>
<link rel="stylesheet" href="/college/style.css">
<form method="post" action="/college/update.py?roll={roll}">
<input type="emai" name="email" value="{result[1]}" placeholder="Your email here">
<input type="name" name="name"value="{result[0]}"placeholder="Your Name here">
<input type="text" name="stream" value="{result[2]}" placeholder="Your stream here">
<input type="password" name="password" value="{result[3]}" placeholder="Your Password here">
<button class="btn" type="submit">Change</button>
<a href="/college/main.py">Cancel</a>
</form>
""")