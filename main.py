#!C:\python 3.8\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
data=cgi.FieldStorage()
name=data.getvalue('name')

style=open('style.css', 'r')
glitch=open('glitch.css', 'r')
nav=open('nav.html', 'r')
if name==None:
    name=' '
print(f"""
<style>{style.read()}</style>
<style>{glitch.read()}</style>
{nav.read()}

<h1 class='center '>Welcome {name} To IIT Kolkata </h1>
""")
glitch.close()
style.close()
nav.close()