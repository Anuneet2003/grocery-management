from tkinter import * 
def userpass(): 
 def c(): 
 return g.get(),h.get() 
 root=Tk() 
 h=StringVar() 
 g=StringVar() 
 root.configure(bg='aqua') 
 root.title('ENTER YOUR DETAILS') 
 c1=0 
 
 def d(): 
 nonlocal pas,g,c1 
 c1+=1 
 pas.destroy() 
 if c1%2!=0: 
 pas=Entry(root,textvariable=h,fg='yellow',bg='blue',font='Ravie 23 bold') 
 pas.grid(row=1,column=1) 
 else: 
 x=Entry(root,textvariable=h,fg='yellow',bg='blue',font='Ravie 23 bold',show='*') 
 x.grid(row=1,column=1) 
 
 Label(root,text='Username: ',fg='blue',bg='aqua',font='Forte 30 bold').grid(row=0,column=0) 
 user=Entry(root,textvariable=g,fg='yellow',bg='blue',font='Ravie 23 bold') 
 user.grid(row=0,column=1) 
 Label(root,text='Password: ',fg='blue',bg='aqua',font='Forte 30 bold').grid(row=1,column=0) 
 pas=Entry(root,textvariable=h,fg='yellow',bg='blue',font='Ravie 23 bold',show='*') 
 pas.grid(row=1,column=1) 
 Button(root,text='submit',fg='yellow',bg='darkblue',font='Forte 16',command=root.destroy).grid(row=2,column=1) 
 Button(root,text='Show',fg='yellow',bg='darkblue',font='Forte 16',command=d).grid(row=1,column=2) 
 root.mainloop() 
 return c() 
##print(userpass()) 
def userdet(): 
 def c(): 
 return g.get(),h.get(),i.get(),j.get() 
 root=Tk() 
 h=StringVar() 
 g=StringVar() 
 i=StringVar() 
 j=StringVar() 
 c1=0 
 
 root.configure(bg='aqua') 
 root.title('ENTER YOUR DETAILS') 
 def d(): 
 nonlocal pas,g,c1 
 c1+=1 
 pas.destroy() 
 if c1%2!=0: 
 pas=Entry(root,textvariable=h,fg='yellow',bg='blue',font='Ravie 23 bold') 
 pas.grid(row=1,column=1) 
 else: 
 x=Entry(root,textvariable=h,fg='yellow',bg='blue',font='Ravie 23 bold',show='*') 
 x.grid(row=1,column=1) 
 
 Label(root,text='Username: ',fg='blue',bg='aqua',font='Forte 30 bold').grid(row=0,column=0) 
 user=Entry(root,textvariable=g,fg='yellow',bg='blue',font='Ravie 23 bold') 
 user.grid(row=0,column=1) 
 Label(root,text='Password: ',fg='blue',bg='aqua',font='Forte 30 bold').grid(row=1,column=0) 
 pas=Entry(root,textvariable=h,fg='yellow',bg='blue',font='Ravie 23 bold',show='*') 
 pas.grid(row=1,column=1) 
 Label(root,text='Mobile: ',fg='blue',bg='aqua',font='Forte 30 bold').grid(row=2,column=0) 
 mob=Entry(root,textvariable=i,fg='yellow',bg='blue',font='Ravie 23 bold') 
 mob.grid(row=2,column=1) 
 Label(root,text='Address: ',fg='blue',bg='aqua',font='Forte 30 bold').grid(row=3,column=0) 
 ad=Entry(root,textvariable=j,fg='yellow',bg='blue',font='Ravie 23 bold') 
 ad.grid(row=3,column=1) 
 Button(root,text='submit',fg='yellow',bg='darkblue',font='Forte 16',command=root.destroy).grid(row=4,column=1) 
 Button(root,text='Show',fg='yellow',bg='darkblue',font='Forte 16',command=d).grid(row=1,column=2) 
 root.mainloop() 
 return c() 
##print(userdet()) 
def secques(): 
 q=input('What\'s your security code?') 
 q1=input('What\'s your last status?') 
 return q,q1 
def intro(): 
 hello=Tk() 
 hello.geometry('740x460') 
 hello.configure(bg='black') 
 hello.title('let\'s shop') 
 Label(hello,text=' Anuneet and Shourya\'s ',fg='orange',bg='purple',font='Magneto 35 bold 
italic').grid(row=0,column=1) 
 Label(hello,text=' Anurya ',fg='purple',bg='violet',font='Jokerman 130 bold').grid(row=1,column=1) 
 Label(hello,text=' GROCERIES ',fg='orange',bg='purple',font='Ravie 31 bold').grid(row=2,column=1) 
 Button(hello,text='LET\'S SHOP',fg='gold',bg='black',font='forte 30 
bold',command=hello.destroy).grid(row=4,column=1) 
 hello.mainloop() 
