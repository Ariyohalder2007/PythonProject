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
<div class='box'><h2> Welcome {name} To Our College Portal</h2><p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem laudantium tenetur recusandae officiis porro, repellat, eius quas earum deserunt sapiente ut vel! Asperiores quaerat commodi nihil fuga aut quas facere temporibus? Quia, delectus. Distinctio! </p> </div>
<div class='box'><h2>!!! {name} Best Of Luck For Exams!!!</h2><p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem laudantium tenetur recusandae officiis porro, repellat, eius quas earum deserunt sapiente ut vel! Asperiores quaerat commodi nihil fuga aut quas facere temporibus? Quia, delectus. Distinctio! </p> </div>
<script src="https://kit.fontawesome.com/2f47edd958.js" crossorigin="anonymous"></script>
""")
style.close()

nav.close()