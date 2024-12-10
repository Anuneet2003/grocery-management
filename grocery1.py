import mysql.connector as sqlc 
x=sqlc.connect(host='localhost',user='root',passwd='*******',database='grocery') 
if x.is_connected()==False: 
 print('Error connecting to database') 
c=x.cursor() 
c.execute('create table customers(Id integer UNIQUE, Name varchar(40), Address varchar(500), Mobile integer, Password varchar(20) UNIQUE)') 
c.execute('create table products(ProdId integer UNIQUE, Brand varchar(40), Prod_Class varchar(100), Prodname varchar(100), Price integer, Inventory integer, Availability char(1))') 
c.execute('create table bill(OrdId integer, Price integer, Items integer,Name varchar(40), Address varchar(500), Mobile integer )') 
c.execute('create table cart(ProdId integer, Brand varchar(40), Prod_Class varchar(100), Prodname varchar(100), Price integer, Qty integer,Name varchar(40), Mobile integer)') 
c.execute('create table cart1(ProdId integer, Brand varchar(40), Prod_Class varchar(100), Prodname varchar(100), Price integer, Qty integer,Name varchar(40), Mobile integer ,Ordertime datetime)') 
c.close() 
x.close()
