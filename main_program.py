from tkinter import *
from tkinter import messagebox
import mysql.connector as my


mydb=my.connect(host="localhost",
                        user="root",
                        password="",
                        database="python")
       
cur=mydb.cursor()


win = Tk()

win.title("Employees Information")
win.geometry("600x600")

def insert():
    id= emp_id.get()
    f_name=first_name.get()
    l_name=last_name.get()
    d = designation.get()
    c = city.get()
    if(id =="" or f_name=="" or l_name=="" or d =="" or c ==""):
        messagebox.showinfo("insert_info","All field are required")
    else:
        cur.execute("Insert into employee (emp_id,first_name,last_name,designation,city)values('"+id+"','"+f_name+"','"+l_name+"','"+d+"','"+c+"')")
        cur.execute("commit");
        e1.delete(0,'end')
        e2.delete(0,'end')
        e3.delete(0,'end')
        e4.delete(0,'end')
        e5.delete(0,'end')
        messagebox.showinfo("Insert_info","Data inserted sucessfully")



def update():
    id= emp_id.get()
    f_name=first_name.get()
    l_name=last_name.get()
    d = designation.get()
    c = city.get()
    if(id =="" or f_name=="" or l_name=="" or d =="" or c ==""):
        messagebox.showinfo("update_info","All field are required")
    else:
        cur.execute("update employee set first_name =('"+f_name+"'),last_name = ('"+l_name+"'),designation = ('"+d+"'),city = ('"+c+"') where emp_id = "+id+"")
        cur.execute("commit");
        e1.delete(0,'end')
        e2.delete(0,'end')
        e3.delete(0,'end')
        e4.delete(0,'end')                                  
        e5.delete(0,'end')
        messagebox.showinfo("Update_info","Data updated sucessfully")                          



def delete():
    id= emp_id.get()
    f_name=first_name.get()
    l_name=last_name.get()
    d = designation.get()
    c = city.get()
    if(id =="" ):
        messagebox.showinfo("Delete_info","Employee ID is required")
    else:
        cur.execute("delete from employee where emp_id = "+id+"")
        cur.execute("commit");
        e1.delete(0,'end')
        e2.delete(0,'end')
        e3.delete(0,'end')
        e4.delete(0,'end')                                  
        e5.delete(0,'end')
        messagebox.showinfo("Delete_info","Data Deleted sucessfully") 


def show():
    cur.execute("select * from employee")
    rows=cur.fetchall()
    list.delete(0,list.size())
    for row in rows:
        data=str(row[0])+' '+row[1]+' '+row[2]+' '+row[3]+' '+row[4]
        list.insert(list.size()+1,data)
    
        
    
emp_id=StringVar()
first_name=StringVar()
last_name=StringVar()
designation=StringVar()
city=StringVar()

lbl1 = Label(win,text = "Employee ID:",foreground = 'white',background = 'blue')
lbl1.grid(row = 0,column =0)
e1 = Entry(win,textvariable = emp_id,bd=5, bg="white")
e1.grid(row=0,column=1)


lbl2 = Label(win,text = "First Name:",width=20)
lbl2.grid(row = 2,column=0)
e2 = Entry(win,textvariable = first_name,bd=5, bg="white")
e2.grid(row=2,column=1)

lbl3 = Label(win,text = "Last Name:",width=20)
lbl3.grid(row = 4,column=0)
e3 = Entry(win,textvariable = last_name,bd=5, bg="white")
e3.grid(row=4,column=1)

lbl4 = Label(win,text = "designation:",width=20)
lbl4.grid(row = 6,column=0)
e4 = Entry(win,textvariable =designation,bd=5, bg="white")
e4.grid(row=6,column=1)



lbl5 = Label(win,text = "City:",width=20)
lbl5.grid(row = 8,column=0)
e5 = Entry(win,textvariable = city,bd=5, bg="white")
e5.grid(row=8,column=1)


b1=Button(win,text="Insert",width=10,relief=RIDGE,foreground = 'white',background = 'blue' ,command=insert)
b1.grid(row=13,column=0)

b2=Button(win,text="Display_all",width=10,relief=RIDGE,foreground = 'white',background = 'blue',command=show)
b2.grid(row=13,column=2)

b3=Button(win,text="Update",width=10,relief=RIDGE,foreground = 'white',background = 'blue',command=update)
b3.grid(row=13,column=4)

b4=Button(win,text="Delete",width=10,relief=RIDGE,foreground = 'white',background = 'blue',command=delete)
b4.grid(row=13,column=6)

list=Listbox(win,width=100,height=20,bd=5)
list.place(x=20,y=180)


win.mainloop()



