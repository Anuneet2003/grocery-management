from grocery5 import * 
import time 
import mysql.connector as sqlc 
x=sqlc.connect(host='localhost',user='root',passwd='Anuneet@2003',database='grocery') 
if x.is_connected()==False: 
 print('\nError connecting to database\n') 
intro() 
#counter 
ch=3 
#choice list for check() function 
choice_list=[1,2,3] 
choice=0 
#Function to avoid value error while asking user to enter a No. of choice 
def check(choice_list): 
 global choice 
 #using try-except for error handling 
 try: 
 choice=int(input('\nEnter your choice')) 
 if choice in choice_list: 
 return choice 
 else: 
 check(choice_list) 
 except ValueError: 
 print('\nValue Error! Try Again!') 
 check(choice_list) 
 return choice 
#Function to check if the mobile no. entered is valid or not 
def check1(): 
 #using try-except for error handling 
 try: 
 mob=int(input('\nEnter Your 10 digit Mobile no.')) 
 if len(str(mob))==10: 
 return mob 
 else: 
 check1() 
 except ValueError: 
 print('\nValue Error! Try Again') 
 check1() 
def menu6(choic,distinct,Name,Mob,Add): 
 c=x.cursor() 
 c.execute("select * from products where Prod_Class='{}'".format(distinct[choic-1][0])) 
 distinct1=c.fetchall() 
 choice_list2=[] 
 for k in distinct1: 
 choice_list2+=[k[0]] 
 print('\nProduct ID->',k[0],'\nBrand->',k[1],'\nProduct->',k[3],'\nPrice->',k[4],'\nStock',k[5],'\n') 
 time.sleep(1) 
 print('\nEnter the Product ID to add that product in your shopping cart') 
 add(choice_list2,choic,Name,Mob,Add,distinct) 
#Function to add the product of choice in shopping cart 
def add(choice_list2,choic,Name,Mob,Add,distinct): 
 c=x.cursor() 
 #using check() for asking product id 
 choice=check(choice_list2) 
 def Quantity(): 
 try: 
 qty=int(input('\nEnter Quantity->')) 
 return qty 
 except: 
 print('Enter valid quantity') 
 Quantity() 
 return qty 
 qty=Quantity() 
 #simple sql command to select Brand,Prod_Class,Prodname,Price from the table products 
 c.execute("select Brand,Prod_Class,Prodname,Price from products where ProdId={}".format(choice)) 
 #fetchall method to fetch all th records as per the condition mentioned above 
 d=c.fetchall() 
 # using double index because d is list containing elements as tuples 
 #tuple unpacking for seperate values of Brand(q),Prod_Class(w),Prodname(e),Price(r) 
 q,w,e,r=d[0][0],d[0][1],d[0][2],d[0][3] 
 #simple sql command to insert all in table cart 
 c.execute("insert into cart(ProdId,Brand,Prod_Class,Prodname,Price,Qty,Name,Mobile) values({},'{}','{}','{}',{},{},'{}',{})".format(choice,q,w,e,r*qty,qty,Name,Mob)) 
 c.execute("insert into cart1(ProdId,Brand,Prod_Class,Prodname,Price,Qty,Name,Mobile,Ordertime) values({},'{}','{}','{}',{},{},'{}',{},sysdate())".format(choice,q,w,e,r*qty,qty,Name,Mob)) 
 c.execute('select ProdId from cart') 
 dup=c.fetchall() 
 for i in dup: 
 i=i 
 if dup.count(i)>1: 
 c.execute("select SUM(Qty) from cart where ProdId={}".format(i[0])) 
 net=c.fetchall() 
 netq=net[0][0] 
 c.execute("delete from cart where ProdId={}".format(i[0])) 
 c.execute("insert into cart(ProdId,Brand,Prod_Class,Prodname,Price,Qty,Name,Mobile) values({},'{}','{}','{}',{},{},'{}',{})".format(choice,q,w,e,r*netq,netq,Name,Mob)) 
 x.commit() 
 #simple sql command to get the inventory stock left 
 c.execute("select Inventory from products where ProdId={}".format(choice)) 
 inv=c.fetchall() 
 #inventory stock before transaction (integer) 
 invtry=inv[0][0] 
 if qty>invtry: 
 print('\nAt present Our stock is less than what you require\nWait for a few minutes till we contact the company as per your requirement') 
 c.execute("update products set Inventory={} where ProdId={}".format(qty+invtry,choice)) 
 x.commit() 
 print('\nWe have arranged the stocks as per your requirement') 
 invtry+=qty 
 #inventory stock left 
 inv1=invtry-qty 
 if inv1>100: 
 c.execute("update products set Inventory={} where ProdId={}".format(inv1,choice)) 
 x.commit() 
 else: 
 c.execute("update products set Inventory={} where ProdId={}".format(1000,choice)) 
 x.commit() 
 #message for choice to user 
 print('\nPress 1 to continue adding products of same variety\nPress 2 to add products of different variety\nPress 3 to view shopping cart') 
 cho=check([1,2,3]) 
 if cho==1: 
 menu6(choic,distinct,Name,Mob,Add) 
 elif cho==2: 
 #if cho==2 break the recursion and returns to superset of this function 
 return 
 elif cho==3: 
 #if cho==3 display user's shopping cart 
 c.execute("select * from cart where Name='{}' and Mobile={}".format(Name,Mob)) 
 d=c.fetchall() 
 for i in d: 
 print(i) 
 time.sleep(1) 
 print('\nReturning to item screen\n Select the item') 
 menu6(choic,distinct,Name,Mob,Add) 
def Psw(): 
 c=x.cursor() 
 Pswd=input('\nEnter New Password') 
 c.execute('select Password from customers') 
 d=c.fetchall() 
 while (Pswd,) in d: 
 print('\nThis Password is already taken! Type another one!') 
 Pswd=input('\nEnter New Password or the Existing one=>') 
 return Pswd 
def Psw1(Name): 
 c=x.cursor() 
 Pswd=input('\nEnter Existing one=>') 
 c.execute("select Password from customers where Name='{}'".format(Name)) 
 d=c.fetchall() 
 if (Pswd,) in d: 
 return Pswd 
 else: 
 print('\nIts not same!!Re enter Existing Password') 
 Psw1(Name) 
 return Pswd 
def menu4(id1,name,pswd,mobi,ad): 
 c=x.cursor() 
 print('\nWelcome to the Grocery store',name,'!!!!') 
 print('\nPress 1 to see your details') 
 choice=check([1]) 
 if choice==1: 
 c=x.cursor() 
 c.execute("select * from customers where Name='{}' and id={}".format(name,id1)) 
 d=c.fetchall() 
 #unpacking tuple for seperate values 
 Name,Pswd,Mob,Add=d[0][1],d[0][4],d[0][3],d[0][2] 
 print('\nID->',d[0][0],'\nName->',d[0][1],'\nPassword->',d[0][4],'\nMobile->',d[0][3],'\nAddress->',d[0][2]) 
 print('\nPress 1 to edit your details\nPress 2 to continue shopping\nPress 3 to exit') 
 choice=check(choice_list) 
 #sub menu to edit your details or to continue shopping or to exit 
 def menu1(Name,Pswd,Mob,Add,choice): 
 c=x.cursor() 
 name,pswd,mobi,ad=Name,Pswd,Mob,Add 
 if choice==1: 
 #to check for duplicate password 
 print('\nPress 1 to write new password\nPress 2 to write existing password') 
 choi=check([1,2]) 
 if choi==1: 
 Pswd=Psw() 
 elif choi==2: 
 Pswd=Psw1(Name) 
 Name=input('\nEnter New Name or the Existing one=>') 
 Mob=check1() 
 Add=input('\nEnter New Address or the Existing one=>') 
 c.execute("update customers set Name='{}',Password='{}',Mobile={},Address='{}' where Name='{}' and Password='{}' and Mobile={} and Address='{}'".format(Name,Pswd,Mob,Add,name,pswd,mobi,ad)) 
 x.commit() 
 print('\nDetails updated successfully!!') 
 c.execute("select * from customers where Name='{}' and id={}".format(Name,id1)) 
 d=c.fetchall() 
 Name,Pswd,Mob,Add=d[0][1],d[0][4],d[0][3],d[0][2] 
 print('\nID->',d[0][0],'\nName->',d[0][1],'\nPassword->',d[0][4],'\nMobile->',d[0][3],'\nAddress->',d[0][2]) 
 print('\nPress 2 to continue shopping\nPress 3 to exit') 
 choice=check([2,3]) 
 if choice==2: 
 menu1(Name,Pswd,Mob,Add,choice=2) 
 elif choice==3: 
 menu1(Name,Pswd,Mob,Add,choice=3) 
 elif choice==2: 
 def menu3(Name,Mob,Add): 
 c=x.cursor() 
 c.execute('select distinct Prod_Class from products') 
 distinct=c.fetchall() 
 j=0#index for choice of various product class like beverages,buiscuits,snacks,etc etc. 
 choice_list1=[] 
 for i in distinct: 
 j+=1 
 choice_list1+=[j] 
 print('\nWe sell=>',i[0]) 
 print('Press \'',j,'\' to shop in \'',i[0],'\'') 
 time.sleep(0.5) 
 ##submenu for addition 
 def menu2(choice_list1,distinct,Name,Mob,Add): 
 c=x.cursor() 
 choic=check(choice_list1) 
 menu6(choic,distinct,Name,Mob,Add) 
 print('\nPress 1 to add products of different variety/same variety\nPress 2 if you are done 
shopping/bill') 
 cho=check([1,2]) 
 if cho==1: 
 #if cho==1 continue adding products using recursion 
 print('\nReturning to choice screen') 
 menu3(Name,Mob,Add) 
 elif cho==2: 
 #if cho==2 display user's bill 
 print('\nPlease check your bill') 
 c.execute("select * from cart where Name='{}' and Mobile={}".format(Name,Mob)) 
 d=c.fetchall() 
 choice_list3=[] 
 for mi in d: 
 choice_list3+=[mi[0]] 
 print(mi) 
 time.sleep(1) 
 print('\nPress 1 to remove an item\nPress 2 to bill') 
 Choice=check([1,2]) 
 def menu5(price,items,Name,Add,Mob,Choice): 
 if Choice==1: 
 def delete(choice_list3): 
 c=x.cursor() 
 print('Enter Product ID to remove') 
 CHOICE=check(choice_list3) 
 c.execute("select Qty from cart where Name='{}' and Mobile={} and 
ProdId={}".format(Name,Mob,CHOICE)) 
 qtyl=c.fetchall() 
 qty=qtyl[0][0] 
 c.execute("select Inventory from products where ProdId={}".format(CHOICE)) 
 invl=c.fetchall() 
 inv=invl[0][0] 
 invn=inv+qty 
 c.execute("update products set Inventory={} where ProdId={}".format(invn,CHOICE)) 
 c.execute("delete from cart where Name='{}' and Mobile={} and 
ProdId={}".format(Name,Mob,CHOICE)) 
 x.commit() 
 print('\nPress 1 to remove more\nPress 2 to stop') 
 CHOIC=check([1,2]) 
 if CHOIC==1: 
 delete(choice_list3) 
 elif CHOIC==2: 
 print('Items removed!!!! Printing Your Bill') 
 print('\nPlease check your bill') 
 c.execute("select * from cart where Name='{}' and Mobile={}".format(Name,Mob)) 
 d=c.fetchall() 
 choice_list3=[] 
 for mi in d: 
 choice_list3+=[mi[0]] 
 print(mi) 
 time.sleep(1) 
 menu5(price,items,Name,Add,Mob,Choice=2) 
 delete(choice_list3) 
 elif Choice==2: 
 c.execute("select SUM(Price) from cart where Name='{}' and Mobile={}".format(Name,Mob)) 
 total=c.fetchall() 
 price=total[0][0] 
 c.execute("select count(*) from cart where Name='{}' and Mobile={}".format(Name,Mob)) 
 total1=c.fetchall() 
 items=total1[0][0] 
 #simple sql command to select all from table cart 
 c.execute('select * from bill') 
 #fetching everything for knowing the rowcount 
 c.fetchall() 
 #creating order id 
 row=c.rowcount+1000000 
 c.execute("insert into bill(OrdId,Price,Items,Name,Address,Mobile) 
values({},{},{},'{}','{}',{})".format(row,price,items,Name,Add,Mob)) 
 x.commit() 
 c.execute("select * from bill where Name='{}' and Mobile={} and 
OrdId={}".format(Name,Mob,row)) 
 d=c.fetchall() 
 for m in d: 
 print('\nOrder ID->',m[0],'\nName->',m[3],'\nMobile->',m[5],'\nTotal Items->',m[2],'\nBill 
Total->',m[1],'\nAddress->',m[4]) 
 print('\nPress 1 to shop again\nPress 2 to exit') 
 Choice=check([1,2]) 
 if Choice==1: 
 c.execute("delete from bill where Name='{}' and Mobile={} and 
OrdId={}".format(Name,Mob,d[0][0])) 
 x.commit() 
 menu3(Name,Mob,Add) 
 else: 
 print('\nTHANK YOU FOR TRUSTING OUR GROCERY STORE!!!!!\nPLEASE COME BACK SOON TO 
SHOP AGAIN ;) :)') 
 c.execute("delete from cart") 
 x.commit() 
 menu5(price,items,Name,Add,Mob,Choice) 
 menu2(choice_list1,distinct,Name,Mob,Add) 
 menu3(Name,Mob,Add) 
 elif choice==3: 
 print('\nTHANK YOU FOR TRUSTING OUR GROCERY STORE!!!!!\nPLEASE COME BACK SOON TO SHOP AGAIN ;) :)') 
 menu1(Name,Pswd,Mob,Add,choice) 
#security question to ensure correct user entry 
def secques(name,pswd,mob,add,id1): 
 c=x.cursor() 
 try: 
 q1=int(input('\nWhat\'s your id?')) 
 except: 
 print('\nwrite integer value') 
 secques(name,pswd,mob,add,id1) 
 if q1==id1: 
 print('\nYour account has been found!\nWELCOME ') 
 menu4(id1,name,pswd,mob,add) 
 else: 
 print('\nYour activity has been suspended,Try again later') 
 
#Function of main menu 
def menu(): 
 #Message for user to ask about his choice when the program begins 
 print('\nPress 1 if you are an existing user\nPress 2 if you are a new user\nPress 3 to exit') 
 #asking user for his choice from the message mentioned above 
 choice=check(choice_list) 
 #creating sql cursor object 
 c=x.cursor() 
 if choice==1: 
 #asking user to enter his name and his password 
 name,pswd=userpass() 
 c.execute("select * from customers where Name='{}' and Password='{}'".format(name,pswd)) 
 d=c.fetchall() 
 if d==[]: 
 print('\nNo account found! Forgot Password!?\n(Press 1 for Yes or Press 2 for No)') 
 choice=check(choice_list) 
 if choice==1: 
 mob=check1() 
 try: 
 c.execute("select Mobile from customers where Name='{}'".format(name)) 
 e=c.fetchall() 
 if (mob,) in e: 
 c.execute("select Id,Address from customers where Name='{}' and Mobile={}".format(name,mob)) 
 e=c.fetchall() 
 id1=e[0][0] 
 add=e[0][1] 
 #security question to ensure correct user entry 
 secques(name,pswd,mob,add,id1) 
 else: 
 c.execute("select Mobile from customers where Password='{}'".format(name)) 
 e=c.fetchall() 
 if (mob,) in e: 
 c.execute("select Id,Address from customers where Password='{}' and 
Mobile={}".format(name,mob)) 
 e=c.fetchall() 
 id1=e[0][0] 
 add=e[0][1] 
 #security question to ensure correct user entry 
 secques(name,pswd,mob,add,id1) 
 else: 
 e=[] 
 except: 
 e=[] 
 if e==[]: 
 #ch is the counter for giving chance to user to enter correct details 
 global ch 
 #decrementing counter 
 ch-=1 
 print('\nNo mobile found for the given name and password!?\nWARNING!!!!!\n(Only ',ch,' chances left 
before blocking your account)') 
 if ch==0: 
 print('\nYour activity has been suspended,Try again later') 
 else: 
 #taking user back to main menu 
 menu() 
 elif choice==2: 
 print('\nNo account found for the given name and password!') 
 choice=1 
 #taking user back to main menu 
 menu() 
 else: 
 c.execute("select * from customers where Name='{}' and Password='{}'".format(name,pswd)) 
 data=c.fetchall() 
 id1,name,pswd,mobi,ad=data[0][0],data[0][1],data[0][4],data[0][3],data[0][2] 
 menu4(id1,name,pswd,mobi,ad) 
 elif choice==2: 
 #user to enter correct details 
 name,pswd,mobi,ad=userdet() 
 c.execute("select Password from customers") 
 pas=c.fetchall() 
 if (pswd,) in pas: 
 pswd=Psw() 
 if len(mobi)<10: 
 mobi=check1() 
 else: 
 mobi=int(mobi) 
 c.execute("select * from customers") 
 c.fetchall() 
 id1=c.rowcount+1 
 c.execute("insert into customers(Id, Name, Address, Mobile, Password) 
values({},'{}','{}',{},'{}')".format(id1,name,ad,mobi,pswd)) 
 #commit to make permanent changes 
 x.commit() 
 menu4(id1,name,pswd,mobi,ad) 
 elif choice==3: 
 print('\nLEAVING SO SOON!!!!!\nPLEASE COME BACK SOON TO SHOP AGAIN ;) :)') 
menu()
