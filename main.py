#!C:\python 3.8\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
head=open("head.txt", 'r')
end=open("end.txt", 'r')
print(head.read())
#code here



print(end.read())
head.close()
end.close()
