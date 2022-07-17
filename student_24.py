from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2



class Student:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1360x700+0+0")
        self.root.title("Face Recognition system")
        self.root.wm_iconbitmap("face.ico")


        #_______________variables________________________
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        # first image
        img1=Image.open(r"E:\Face recogniton project\pictures\smart-attendance.jpg")
        img1=img1.resize((450,80),Image.ANTIALIAS)
        self.pic_img1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.pic_img1)
        f_lbl.place(x=0,y=0,width=450,height=80)


        # second image
        img2=Image.open(r"E:\Face recogniton project\pictures\Face-Recognition-Student.jpg")
        img2=img2.resize((450,80),Image.ANTIALIAS)
        self.pic_img2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.pic_img2)
        f_lbl.place(x=450,y=0,width=450,height=80)


        # third image
        img3=Image.open(r"E:\Face recogniton project\pictures\student3.gif")
        img3=img3.resize((460,80),Image.ANTIALIAS)
        self.pic_img3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.pic_img3)
        f_lbl.place(x=900,y=0,width=460,height=80)



        # bg image
        img4=Image.open(r"E:\Face recogniton project\pictures\Artificial.jpg")
        img4=img4.resize((1360,620),Image.ANTIALIAS)
        self.pic_img4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.pic_img4)
        bg_img.place(x=0,y=80,width=1360,height=620)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen" )
        title_lbl.place(x=0,y=0,width=1360,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1340,height=670)


        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=685,height=545)

        left_img=Image.open(r"E:\Face recogniton project\pictures\face_3.jpg")
        left_img=left_img.resize((670,90),Image.ANTIALIAS)
        self.pic_img_left=ImageTk.PhotoImage(left_img)

        f_lbl=Label(Left_frame,image=self.pic_img_left)
        f_lbl.place(x=5,y=0,width=670,height=90)



        # current course information
        current_course=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course.place(x=5,y=95,width=670,height=120)

        #Department
        dep_label=Label(current_course,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","EXTC")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #course
        course_label=Label(current_course,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(current_course,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)

        semester_combo=ttk.Combobox(current_course,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Class Student  information
        class_student=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student.place(x=5,y=215,width=670,height=300)

        #student id
        student_id_label=Label(class_student,text="Student ID :",font=("times new roman",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        student_entry=ttk.Entry(class_student,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        student_entry.grid(row=0,column=1,padx=10,sticky=W)

        #student name
        student_name_label=Label(class_student,text="Student Name :",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        student_name_entry=ttk.Entry(class_student,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,sticky=W)

        #student division
        class_div_label=Label(class_student,text="Class Division :",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        

        div_combo=ttk.Combobox(class_student,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=18)
        div_combo["values"]=("Select Division","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        # roll no
        roll_no_label=Label(class_student,text="Roll No :",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,sticky=W)

        #Gender
        gender_label=Label(class_student,text="Gender :",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        

        gender_combo=ttk.Combobox(class_student,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)

        #Dob
        dob_label=Label(class_student,text="DOB :",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_student,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,sticky=W)

        #Email
        email_label=Label(class_student,text="Email :",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_student,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,sticky=W)

        #phone no
        phone_label=Label(class_student,text="Phone No :",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(class_student,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,sticky=W)

        #Address
        address_label=Label(class_student,text="Address :",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_student,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,sticky=W)

        #teacher
        teacher_label=Label(class_student,text="Teacher :",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(class_student,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,sticky=W)

        # radio button
        self.var_radio=StringVar()
        radio_btn1=ttk.Radiobutton(class_student,variable=self.var_radio,text="Take Photo Sample",value="Yes")
        radio_btn1.grid(row=5,column=0)


        radio_btn2=ttk.Radiobutton(class_student,variable=self.var_radio,text="No Photo Sample",value="No")
        radio_btn2.grid(row=5,column=1)

        # button frame
        btn_frame=Frame(class_student,bd=2,relief=RIDGE,bg="White")
        btn_frame.place(x=0,y=200,width=650,height=35)

        # save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="White")
        save_btn.grid(row=0,column=0)

        # update button
        update_btn=Button(btn_frame,text="Update",command=self.Update_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="White")
        update_btn.grid(row=0,column=1)

        # delete button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="White")
        delete_btn.grid(row=0,column=2)

        # reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="White")
        reset_btn.grid(row=0,column=3)

        #down frame
        btn_1_frame=Frame(class_student,bd=2,relief=RIDGE,bg="White")
        btn_1_frame.place(x=0,y=235,width=650,height=35)

        # take_photo button
        take_photo_btn=Button(btn_1_frame,command=self.generate_dataset,text="Take Photo Sample",width=31,font=("times new roman",13,"bold"),bg="blue",fg="White")
        take_photo_btn.grid(row=0,column=0)

        # update_photo button
        update_photo_btn=Button(btn_1_frame,text="Update Photo Sample",width=32,font=("times new roman",13,"bold"),bg="blue",fg="White")
        update_photo_btn.grid(row=0,column=1)







        # Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=700,y=10,width=625,height=545)



        right_img=Image.open(r"E:\Face recogniton project\pictures\face_recognition_4.jpg")
        right_img=right_img.resize((610,90),Image.ANTIALIAS)
        self.pic_img_right=ImageTk.PhotoImage(right_img)

        f_lbl=Label(Right_frame,image=self.pic_img_right)
        f_lbl.place(x=5,y=0,width=610,height=90)


        #______________search system__________________
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=100,width=605,height=70)

        search_label=Label(search_frame,text="Search By :",font=("times new roman",14,"bold"),bg="orange",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=13)
        search_combo["values"]=("Select ","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=13,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,sticky=W)

        search_btn=Button(search_frame,text="Search",width=11,font=("times new roman",11,"bold"),bg="blue",fg="White")
        search_btn.grid(row=0,column=3,padx=4)

        
        ShowAll_btn=Button(search_frame,text="Show All",width=11,font=("times new roman",11,"bold"),bg="blue",fg="White")
        ShowAll_btn.grid(row=0,column=4,padx=4)
        

        #_______________table frame____________________
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=180,width=605,height=340)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #________________________function definition__________________
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Reqiured",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="pass1word",database="face_recognizer1")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio.get()


                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details are Successfully added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    #________________fetch data______________________
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="pass1word",database="face_recognizer1")
        my_cursor=conn.cursor()
        my_cursor.execute("select *from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #________________get cursor_______________________
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8])
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio.set(data[14])
    


    # update function
    def Update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Reqiured",parent=self.root)

        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="pass1word",database="face_recognizer1")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s",(

                                                                                                                                                                                
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio.get(),
                                                                                                                                                                                    self.var_std_id.get()     
                                                                                                                                                                                
                                                                                                                                                                                ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully updated completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

        


    


    # delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be resigter",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)

                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="pass1word",database="face_recognizer1")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    # reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio.set("")


    #________________generate data set or take photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Reqiured",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="pass1word",database="face_recognizer1")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s",(

                                                                                                                                                                                
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio.get(),
                                                                                                                                                                                    self.var_std_id.get()==id+1    
                                                                                                                                                                                
                                                                                                                                                                                ))
                self.fetch_data()
                self.reset_data()
                conn.close()

                #_______________________Load predefined data on face frontals from opencv______________________

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed !!!",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


        

                

        

        




if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
