#!C:\python 3.8\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi

style=open('style.css', 'r')
nav=open('nav.html', 'r')

print(f"""
<style>{style.read()}</style>
{nav.read()}

<title>
IIT Kolkata
</title>
<h1 class='center '>Contact Us</h1>
<form method="post" action="send_mail.py">
 		<input type="name" style="width: 29rem;" name="name" placeholder="Your Name">
 		<input type="email"  style="width: 29rem;" name="email" placeholder="Your Email">
		 <input type="number"  style="width: 29rem;" name="roll" placeholder="Your Roll N.O.">
         <textarea style="width: 29rem;" name="reason" placeholder="Reason for contacting"></textarea>
 		<button type="submit" class="btn">Submit</button>
 	</form>
<script src="https://kit.fontawesome.com/2f47edd958.js" crossorigin="anonymous"></script>
""")
style.close()
nav.close()