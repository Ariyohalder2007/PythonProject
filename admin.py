#!C:\python 3.8\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
try:
  
    data=cgi.FieldStorage()
    name=data.getvalue('name')
    password=data.getvalue('password')
    
    if password ==  "ariyo2007" and name == "ariyo":
        print("""<link rel="stylesheet" type="text/css" href="style.css">
        <h1 class='center'>You are successfully LoggedIn <a style='text-decoration:none;' href='adminin.py/'> Click Here</a></h1>""")
    else:
        print("""<link rel="stylesheet" type="text/css" href="style.css">
        <h1 class='center' style='color:red;'>Wrong Details!!!!!</h1>""")
  
except Exception as e:
    print(e)
