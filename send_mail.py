#!C:\python 3.8\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import smtplib


def sendEmail(sender, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('alokhalder6359@gmail.com', 'sinjhini')
    server.sendmail(sender, 'alokhalder6359@gmail.com', content)
    server.close()

style=open('style.css', 'r')
nav=open('nav.html', 'r')
data=cgi.FieldStorage()
name=data.getvalue('name')
email=data.getvalue('email')
roll=data.getvalue('roll')
reason=data.getvalue('reason')
content=f"""
I am {name}
with roll n.o. {roll} reading in your college
I need help For the Following Reason:
{reason}
my email-id is {email}
"""
try:
    sendEmail(email, content)
    print(f"""
    <style>
    {style.read()}
    </style>
    {nav.read()}
    <h2 style="margin-top:10px; color:green;" class='center'> Sent Successfully Thanks For Contacting. We will Be In Touch With You Shortly. You Can Now Go Back to DashBoard</h2>
    <script src="https://kit.fontawesome.com/2f47edd958.js" crossorigin="anonymous"></script>
    """)
except Exception as e:
    print(e)


