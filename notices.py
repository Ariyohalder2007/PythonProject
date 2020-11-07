#!C:\python 3.8\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
data=cgi.FieldStorage()
db=mysql.connector.connect(host="127.0.0.1",user="root",password="",db="college")
cursor=db.cursor()

sql="select * from notices"
cursor.execute(sql)

result=cursor.fetchall()
db.commit()
style=open('style.css', 'r')
nav=open('nav.html', 'r')

print(f"""
<style>{style.read()}</style>
{nav.read()}

<title>
IIT Kolkata
</title>
<h1 class='center'> Notices</h1>
<script src="https://kit.fontawesome.com/2f47edd958.js" crossorigin="anonymous"></script>
""")
print("""<table border="1" align="center">
<tr>
<td><h3>Name</h3></td>
<td><h3>Description</h3></td>
<td><h3>Publish Date</h3></td>
</tr>

""")
for i in range(len(result)):
	print("""
	<tr>
	""")
	for j in result[i]:
		print("""
		<td>""")
		
		print(j)
		print("""
		</td>""")
	print("""
	</tr>
	""")
print("""</table""")
style.close()
nav.close()
db.close()
cursor.close()