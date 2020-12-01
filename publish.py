#!C:\python 3.8\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector

try:
    db=mysql.connector.connect(host="127.0.0.1",user="root",password="",db="college")
    cursor=db.cursor()
    data=cgi.FieldStorage()
    heading=data.getvalue('heading')
    content=data.getvalue('content')
    publish_date=str(data.getvalue('publish_date'))
    sql_query="insert into notices values('%s','%s','%s')"%(heading , content, publish_date )
    cursor.execute(sql_query)
    db.commit()
    print("""
        <link rel="stylesheet" type="text/css" href="style.css">
        <h1 class='center'>SUCCESFULLY published<a style='text-decoration:none;' href='/college/adminin.py'> Click Here to Go to Admin</a></h1>
        """)
    
except Exception as e:
    print(e)

