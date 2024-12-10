import mysql.connector as sqlc 
x=sqlc.connect(host='localhost',user='root',passwd='******') 
if x.is_connected()==False: 
 print('Error connecting to database') 
c=x.cursor() 
c.execute('create database grocery') 
c.close() 
x.close()
