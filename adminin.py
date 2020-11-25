#!C:\python 3.8\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
data=cgi.FieldStorage()

style=open('style.css', 'r')
nav=open('adminnav.html', 'r')

print(f"""
<style>{style.read()}</style>
{nav.read()}

<title>
IIT Kolkata
</title> 
<h1 class='center '>Welcome To IIt Kolkata Admin </h1>
<h2 class="center">You Can See Student and Publish Notices</h2>
<script src="https://kit.fontawesome.com/2f47edd958.js" crossorigin="anonymous"></script>
""")
style.close()

nav.close()