from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2
import os 
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1360x700+0+0")
        self.root.title("Attendance Management system")
        self.root.wm_iconbitmap("face.ico")

        #=================variables======================
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_status=StringVar()



        # first image
        img1=Image.open(r"pictures\clg.jpg")
        img1=img1.resize((450,150),Image.ANTIALIAS)
        self.pic_img1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.pic_img1)
        f_lbl.place(x=0,y=0,width=450,height=150)


        # second image
        img2=Image.open(r"pictures\Face-Recognition-Student.jpg")
        img2=img2.resize((450,150),Image.ANTIALIAS)
        self.pic_img2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.pic_img2)
        f_lbl.place(x=450,y=0,width=450,height=150)


        # third image
        img3=Image.open(r"pictures\student3.gif")
        img3=img3.resize((460,150),Image.ANTIALIAS)
        self.pic_img3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.pic_img3)
        f_lbl.place(x=900,y=0,width=460,height=150)



        # bg image
        img4=Image.open(r"pictures\Artificial.jpg")
        img4=img4.resize((1360,550),Image.ANTIALIAS)
        self.pic_img4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.pic_img4)
        bg_img.place(x=0,y=150,width=1360,height=550)
        
        title_lbl=Label(bg_img,text="STUDENT ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkblue" )
        title_lbl.place(x=0,y=0,width=1360,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1340,height=600)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT INFORMATION",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=685,height=470)

        left_img=Image.open(r"pictures\face_3.jpg")
        left_img=left_img.resize((670,120),Image.ANTIALIAS)
        self.pic_img_left=ImageTk.PhotoImage(left_img)

        f_lbl=Label(Left_frame,image=self.pic_img_left)
        f_lbl.place(x=5,y=0,width=670,height=120)



        # current course information
        class_student=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE)
        class_student.place(x=5,y=125,width=670,height=320)

         #student id
        student_id_label=Label(class_student,text="Student ID :",font=("times new roman",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        student_entry=ttk.Entry(class_student,width=20,textvariable=self.var_attend_id,font=("times new roman",12,"bold"))
        student_entry.grid(row=0,column=1,padx=10,sticky=W)

        # roll no
        roll_no_label=Label(class_student,text="Roll No :",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student,width=20,textvariable=self.var_attend_roll,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=0,column=3,padx=10,sticky=W)

        #student name
        student_name_label=Label(class_student,text="Student Name :",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        student_name_entry=ttk.Entry(class_student,width=20,textvariable=self.var_attend_name,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=10,sticky=W)

        # Dep
        dep_label=Label(class_student,text="Department :",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        dep_entry=ttk.Entry(class_student,width=20,textvariable=self.var_attend_dep,font=("times new roman",12,"bold"))
        dep_entry.grid(row=1,column=3,padx=10,sticky=W)

        # time
        time_label=Label(class_student,text="Time :",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        time_entry=ttk.Entry(class_student,width=20,textvariable=self.var_attend_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,padx=10,sticky=W)

        # Date
        Date_label=Label(class_student,text="Date :",font=("times new roman",12,"bold"),bg="white")
        Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        Date_entry=ttk.Entry(class_student,width=20,textvariable=self.var_attend_date,font=("times new roman",12,"bold"))
        Date_entry.grid(row=2,column=3,padx=10,sticky=W)

        #student attendance
        class_div_label=Label(class_student,text="Attendance status :",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        

        div_combo=ttk.Combobox(class_student,font=("times new roman",12,"bold"),textvariable=self.var_attend_status,state="readonly",width=18)
        div_combo["values"]=("Status","Present","Absent")
        div_combo.current(0)
        div_combo.grid(row=3,column=1,padx=2,pady=5,sticky=W)

        # button frame
        btn_frame=Frame(class_student,bd=2,relief=RIDGE,bg="White")
        btn_frame.place(x=0,y=270,width=665,height=35)

        # import button
        import_btn=Button(btn_frame,text="Import CSV",command=self.import_csv,width=16,font=("times new roman",13,"bold"),bg="blue",fg="White")
        import_btn.grid(row=0,column=0)

        # export button
        export_btn=Button(btn_frame,text="Export CSV",command=self.export_csv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="White")
        export_btn.grid(row=0,column=1)

        # Update button
        update_btn=Button(btn_frame,text="Update",width=16,font=("times new roman",13,"bold"),bg="blue",fg="White")
        update_btn.grid(row=0,column=2)

        # reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="White")
        reset_btn.grid(row=0,column=3)


        # Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=700,y=10,width=625,height=470)



        # right_img=Image.open(r"E:\Face recogniton project\pictures\face_recognition_4.jpg")
        # right_img=right_img.resize((610,120),Image.ANTIALIAS)
        # self.pic_img_right=ImageTk.PhotoImage(right_img)

        # f_lbl=Label(Right_frame,image=self.pic_img_right)
        # f_lbl.place(x=5,y=0,width=610,height=120)


        #_______________table frame____________________
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=10,width=605,height=430)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("id","roll","name","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("time",text="Time")
        self.student_table.heading("date",text="Date")
        self.student_table.heading("attendance",text="Attendance")
        self.student_table["show"]="headings"


        self.student_table.column("id",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("time",width=100)
        self.student_table.column("date",width=100)
        self.student_table.column("attendance",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        # self.fetch_data()

    #================fetch data===========================
    def fetch_data(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)
    #=================import csv==============
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    #===================export csv====================
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","NO Data Found to Export",parent=self.root)
                return False
            
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+" Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #===================get cursor====================
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_status.set(rows[6])
        self.var_attend_id.set(rows[0])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_status.set("")
        self.var_attend_id.set("")




       


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
