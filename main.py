#!C:\python 3.8\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
data=cgi.FieldStorage()
name=data.getvalue('name')

style=open('style.css', 'r')
nav=open('nav.html', 'r')
if name==None:
    name=' '
print(f"""
<style>{style.read()}</style>
{nav.read()}

<title>
IIT Kolkata
</title>
<h1 class='center '>Welcome {name} To IIT Kolkata </h1>
<script src="https://kit.fontawesome.com/2f47edd958.js" crossorigin="anonymous"></script>
""")
style.close()
nav.close()