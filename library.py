from tkinter import *

from tkinter import ttk

import mysql.connector

from tkinter import messagebox

import datetime




class LibraryManagementSystem:

    def __init__(self,root):
        self.root=root

        self.root.title("BAIUST LIBRARY MANAGAMENT SYSTEM")

        self.root.geometry("1550x800+0+0")
        
        

        #================Variable===============
        

        self.member_var=StringVar()

        self.ID_var=StringVar()

        self.Name_var=StringVar()

        self.Department_var=StringVar()

        self.Phone_var=StringVar()

        self.BookID_var=StringVar()

        self.BookName_var=StringVar()

        self.DateOfBorrow_var=StringVar()

        self.DateOfReturn_var=StringVar()

        self.FineForLate_var=StringVar()

        self.BookPrice_var=StringVar()

        self.FineForlost_var=StringVar()
        

        #=========================================
        

        lbtitle = Label(self.root,text="BAIUST LIBRARY MANAGEMENT SYSTEM",bg="green",fg="white",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=10,pady=16)

        lbtitle.pack(side=TOP,fill=X)
        

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")

        frame.place(x=0,y=130,width=1550,height=400)

        #===================Left Frame ==============#

        DataFrameLeft=LabelFrame(frame,text="Library Membership Info",bg="powder blue",fg="black",bd=12,relief=RIDGE,font=("times new roman",15,"bold"))

        DataFrameLeft.place(x=0,y=5,width=900,height=350)
        
        

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Choose Member Type",font=("times new roman",12,"bold"),padx=2,pady=6)

        lblMember.grid(row=0,column=0,sticky=W)
        

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),width=27,state="readonly")

        comMember["value"]=("Admin Staf","Lecuturer","Professor","Student")

        comMember.grid(row=0,column=1)
        

        lblID_No=Label(DataFrameLeft,bg="powder blue",text="ID Number",font=("times new roman",12,"bold"),padx=2,pady=6)

        lblID_No.grid(row=1,column=0,sticky=W)

        txtID_No=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.ID_var,width=36) 

        txtID_No.grid (row=1,column=1)
        

        lbl_Name = Label(DataFrameLeft,text="Name",font=("times new roman",12,"bold"),bg="powder blue",padx=2,pady=6)

        lbl_Name.grid(row=2,column=0,sticky=W)

        txt_Name = Entry(DataFrameLeft,font=("times new roman",12),textvariable=self.Name_var,width=36)

        txt_Name.grid(row=2,column=1)
        

        lbl_dept = Label(DataFrameLeft,text="Department",font=("times new roman",12,"bold"),bg="powder blue",padx=2,pady=6)

        lbl_dept.grid(row=3,column=0,sticky=W)

        comdept=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),width=27,state="readonly")

        comdept["value"]=("CSE","EEE","CE","ENG")

        comdept.grid(row=3,column=1)
        

        lbl_phone = Label(DataFrameLeft,text="Phone Number",font=("times new roman",12,"bold"),bg="powder blue",padx=2,pady=6)

        lbl_phone.grid(row=4,column=0,sticky=W)

        txt_phone = Entry(DataFrameLeft,font=("times new roman",12),textvariable=self.Phone_var,width=36)

        txt_phone.grid(row=4,column=1)
        

        lbl_BookID = Label(DataFrameLeft,text="Book ID",font=("times new roman",12,"bold"),bg="powder blue",padx=2,pady=6)

        lbl_BookID.grid(row=5,column=0,sticky=W)

        txt_BookID = Entry(DataFrameLeft,font=("times new roman",12),textvariable=self.BookID_var,width=36)

        txt_BookID.grid(row=5,column=1)
        

        lbl_Booktitle = Label(DataFrameLeft,text="Book Name",font=("times new roman",12,"bold"),bg="powder blue",padx=2,pady=6)

        lbl_Booktitle.grid(row=6,column=0,sticky=W)

        txt_Booktitle = Entry(DataFrameLeft,font=("times new roman",12),width=36,textvariable=self.BookName_var)

        txt_Booktitle.grid(row=6,column=1)
        

        lbl_DateofBorrow = Label(DataFrameLeft,text="Date Of Borrow",font=("times new roman",12,"bold"),bg="powder blue",padx=2,pady=6)

        lbl_DateofBorrow.grid(row=7,column=0,sticky=W)

        txt_DateofBorrow = Entry(DataFrameLeft,font=("times new roman",12),width=36,textvariable=self.DateOfBorrow_var)

        txt_DateofBorrow.grid(row=7,column=1)
        

        lbl_DateofReturn = Label(DataFrameLeft,text="Date Of Return",font=("times new roman",12,"bold"),bg="powder blue",padx=2,pady=6)

        lbl_DateofReturn.grid(row=8,column=0,sticky=W)

        txt_DateofReturn = Entry(DataFrameLeft,font=("times new roman",12),textvariable=self.DateOfReturn_var,width=36)

        txt_DateofReturn.grid(row=8,column=1)
        

        lbl_Fineforlatesub = Label(DataFrameLeft,text="Fine For Late",font=("times new roman",12,"bold"),bg="powder blue",padx=2,pady=6)

        lbl_Fineforlatesub.grid(row=0,column=2,sticky=W)

        txt_Fineforlatesub = Entry(DataFrameLeft,font=("times new roman",12),textvariable=self.FineForLate_var,width=36)

        txt_Fineforlatesub.grid(row=0,column=3)
        

        lbl_BookPrice = Label(DataFrameLeft,text="Book Price",font=("times new roman",12,"bold"),bg="powder blue",padx=2,pady=6)

        lbl_BookPrice.grid(row=1,column=2,sticky=W)

        txt_BookPrice = Entry(DataFrameLeft,font=("times new roman",12),textvariable=self.BookPrice_var,width=36)

        txt_BookPrice.grid(row=1,column=3)
        

        lbl_lostfine = Label(DataFrameLeft,text="Fine For Lost",font=("times new roman",12,"bold"),bg="powder blue",padx=2,pady=6)

        lbl_lostfine.grid(row=2,column=2,sticky=W)

        txt_lostfine = Entry(DataFrameLeft,font=("times new roman",12),textvariable=self.FineForlost_var,width=36)

        txt_lostfine.grid(row=2,column=3)
        
        

        #===================Right Frame ==============#

        DataFrameRight=LabelFrame(frame,text="Book Info",bg="powder blue",fg="black",bd=12,relief=RIDGE,font=("times new roman",15,"bold"))

        DataFrameRight.place(x=910,y=5,width=540,height=350)
        

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=12) 

        self.txtBox.grid(row=0,column=2)
        
        

        listScroll=Scrollbar(DataFrameRight)

        listScroll.grid(row=0,column=1,sticky="ns")
        
        

        listBook=['Premer Tane','Python er Prem','Code Amar Mathay Dhuke Na','C Programming','Give and Take','Best Friend','Best Eleven','Army Life','GUI Python','What A Life','Waitning For You','Buy And Sell','Its Love','Titanic']
        

        def SelectBook(event=""):

            value=str(listBox.get(listBox.curselection))

            x=value

            if (x=="Premer Tane"):

                self.BookID_var.set("0001")

                self.BookName_var.set("Premer Tane")
                

                d1=datetime.datetime.today()

                d2=datetime.timedelta(days=15)

                d3=d1+d2 

                self.DateOfBorrow_var.set(d1)

                self.DateOfReturn_var.set(d3) 

                self.FineForLate_var.set("50")

                self.BookPrice_var.set("500")

                self.FineForlost_var.set("1000")
                              
        
        

        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=22,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScroll.config(command=listBox.yview)
        

        for item in listBook:

            listBox.insert(END,item)
        
        
        
        
        
        

        #===================Buttons Frame ==============#

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="green")

        Framebutton.place(x=0,y=530,width=1950,height=70) 
              

        btnAdddate=Button(Framebutton,text="Add Data",command=self.adda_data,font=("arial",12,"bold"),width=23,bg="red",fg="white")

        btnAdddate.grid(row=0,column=0) 

        btnAdddate=Button(Framebutton,text="Show Data",font=("arial",12,"bold"),width=23,bg="red",fg="white")

        btnAdddate.grid(row=0,column=1) 

        btnAdddate=Button(Framebutton,text="Delete",font=("arial",12,"bold"),width=23,bg="red",fg="white")

        btnAdddate.grid(row=0,column=2) 

        btnAdddate=Button(Framebutton,text="Reset",font=("arial",12,"bold"),width=23,bg="red",fg="white")

        btnAdddate.grid(row=0,column=3) 

        btnAdddate=Button(Framebutton,text="Print",font=("arial",12,"bold"),width=23,bg="red",fg="white")

        btnAdddate.grid(row=0,column=4) 

        btnAdddate=Button(Framebutton,text="Exit",font=("arial",12,"bold"),width=23,bg="red",fg="white")

        btnAdddate.grid(row=0,column=5)
        
        

        #========================Information Frame=======================#

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")

        FrameDetails.place(x=0,y=590,width=1530,height=210)
        
        

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")

        Table_frame.place(x=0,y=2,width=1460,height=190)
        

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)

        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        
        
        
        

        self.library_table=ttk.Treeview(Table_frame,columns=("Member Type","ID Number","Name","Department","Phone Number","Book ID","Book Name","Date Of Borrow","Date Of Return","Fine For Late","Fine For Late","Fine For Lost"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        

        xscroll.pack(side=BOTTOM,fill=X)

        yscroll.pack(side=RIGHT,fill=Y)
        

        xscroll.config(command=self.library_table.xview)

        yscroll.config(command=self.library_table.yview)
        
        

        self.library_table.heading("Member Type",text="Member Type")

        self.library_table.heading("ID Number",text="ID Number")

        self.library_table.heading("Name",text="Name")

        self.library_table.heading("Department",text="Department")

        self.library_table.heading("Phone Number",text="Phone Number")

        self.library_table.heading("Book ID",text="Book ID")

        self.library_table.heading("Book Name",text="Book Name")

        self.library_table.heading("Date Of Borrow",text="Date Of Borrow")

        self.library_table.heading("Date Of Return",text="Date Of Return")

        self.library_table.heading("Fine For Late",text="Fine For Late")

        self.library_table.heading("Fine For Lost",text="Fine For Lost")
      
        

        self.library_table["show"]="headings"

        self.library_table.pack(fill=BOTH,expand=1)
        
        

        self.library_table.column("Member Type",width=100)

        self.library_table.column("ID Number",width=100)

        self.library_table.column("Name",width=100)

        self.library_table.column("Department",width=100)

        self.library_table.column("Phone Number",width=100)

        self.library_table.column("Book ID",width=100)

        self.library_table.column("Book Name",width=100)

        self.library_table.column("Date Of Borrow",width=100)

        self.library_table.column("Date Of Return",width=100)

        self.library_table.column("Fine For Late",width=100)

        self.library_table.column("Fine For Lost",width=100)
        
        

#===================Datebase Connection=======================



    def adda_data(self):

        conn=mysql.connector(host="localhost",username="root",password="kkkkssss",database="baiust")

        my_cursor=conn.cursor()

        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                self.member_var.get(), 

                                                                                                self.ID_var.get(),

                                                                                                self.Name_var.get(),

                                                                                                self.Department_var.get(),

                                                                                                self.Phone_va.get(),

                                                                                                self.BookID_var.get(),

                                                                                                self.BookName_var.get(),

                                                                                                self.DateOfBorrow_var.get(),

                                                                                                self.DateOfReturn_var.get(),

                                                                                                self.FineForLate_var.get(),

                                                                                                self.BookPrice_var.get(),

                                                                                                self.FineForlost_var.get(),
                                                                                            ))

        conn.commit()   

        conn.close()
        

        messagebox.showinfo("Suceess")                                                                        
                                                                                            
        
        
        

if __name__ == "__main__":

    root=Tk()

    obj=LibraryManagementSystem(root)

    root.mainloop()