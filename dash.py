from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from catagory import categoryClass
from product import productClass
from sales import salesClass
import sqlite3
from tkinter import messagebox
import os 
import time
class IMS:
    def __init__(self,root,):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("time new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #btn
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("time  new romen",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=50,width=150)

        #clock
        self.lbl_clock=Label(self.root,text="Welcome\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("time new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #MENU

        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((190,190))
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_MenuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_MenuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")


        lbl_Menu=Label(LeftMenu,text="Menu",font=("time  new romen",20),bg="#009688").pack(side=TOP,fill="x")
        btn_employee=Button(LeftMenu,text="Employee",image=self.icon_side,compound=LEFT,padx=5,anchor="w",command=self.employee, font=("time  new romen",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",image=self.icon_side,compound=LEFT,padx=5,anchor="w",command=self.supplier,font=("time  new romen",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_catagory=Button(LeftMenu,text="Catagory",image=self.icon_side,compound=LEFT,padx=5,anchor="w",command=self.catagory,font=("time  new romen",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",image=self.icon_side,compound=LEFT,padx=5,anchor="w",command=self.product,font=("time  new romen",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",image=self.icon_side,compound=LEFT,padx=5,anchor="w",command=self.sales,font=("time  new romen",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("time  new romen",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #content

        self.lbl_employee=Label(self.root,text="Total Employee \n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_catagory=Label(self.root,text="Total Catagory\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_catagory.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)


        #footer
        lbl_footer=Label(self.root,text="IMS inventory Management System | Develop by Apple \n Conteact: 70xxxxxx70 ",font=("time new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)

        self.update_contact()

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)  

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def catagory(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win) 

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def update_contact(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
                cur.execute("select * from product")
                product=cur.fetchall()
                self.lbl_product.config(text=f'Total Product \n[ {str(len(product))} ]')

                cur.execute("select * from supplier")
                supplier=cur.fetchall()
                self.lbl_supplier.config(text=f'Total Supplier \n[ {str(len(supplier))} ]')

                cur.execute("select * from category")
                category=cur.fetchall()
                self.lbl_catagory.config(text=f'Total Category \n[ {str(len(category))} ]')

                cur.execute("select * from employee")
                employee=cur.fetchall()
                self.lbl_employee.config(text=f'Total Employee \n[ {str(len(employee))} ]')
                bill=len(os.listdir('bill'))
                self.lbl_sales.config(text=f'Total Sales\n [{str(bill)}]')

                time_=time.strftime("%I :%M:%S")
                date_=time.strftime("%d-%m-%Y")
                self.lbl_clock.config(text=f"Welcome\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
                self.lbl_clock.after(200,self.update_contact)
        

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")        
    
                       

if __name__=="__main__":
    root=Tk()
    object=IMS(root)
    root.mainloop()         