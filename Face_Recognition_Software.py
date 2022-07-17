from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import os
from student_24 import Student
from train import Train
from face_recog3 import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_system:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1360x700+0+0")
        self.root.title("Face Recognition system")
        self.root.wm_iconbitmap("face.ico")

        # first image
        img1=Image.open(r"pictures\university.jpg")
        img1=img1.resize((450,130),Image.ANTIALIAS)
        self.pic_img1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.pic_img1)
        f_lbl.place(x=0,y=0,width=450,height=130)


        # second image
        img2=Image.open(r"pictures\face_recognition.png")
        img2=img2.resize((450,130),Image.ANTIALIAS)
        self.pic_img2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.pic_img2)
        f_lbl.place(x=450,y=0,width=450,height=130)


        # third image
        img3=Image.open(r"pictures\university3.jpeg")
        img3=img3.resize((460,130),Image.ANTIALIAS)
        self.pic_img3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.pic_img3)
        f_lbl.place(x=900,y=0,width=460,height=130)

        # bg image
        img4=Image.open(r"pictures\Artificial.jpg")
        img4=img4.resize((1360,570),Image.ANTIALIAS)
        self.pic_img4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.pic_img4)
        bg_img.place(x=0,y=130,width=1360,height=570)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red" )
        title_lbl.place(x=0,y=0,width=1360,height=45)

        #=====================time==========================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text =string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        # student button
        img5=Image.open(r"pictures\student.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.pic_img5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.pic_img5,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=75,width=200,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=245,width=200,height=40)

        # detect face button
        img6=Image.open(r"pictures\face_detect.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.pic_img6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.pic_img6,cursor="hand2",command=self.face_data)
        b1.place(x=450,y=75,width=200,height=200)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=450,y=245,width=200,height=40)


        # Attendance button
        img7=Image.open(r"pictures\attendance_45.png")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.pic_img7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.pic_img7,cursor="hand2",command=self.attendance)
        b1.place(x=750,y=75,width=200,height=200)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=750,y=245,width=200,height=40)


         # Help disk button
        img8=Image.open(r"pictures\help_desk.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.pic_img8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.pic_img8,cursor="hand2",command=self.help_desk)
        b1.place(x=1050,y=75,width=200,height=200)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_desk,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1050,y=245,width=200,height=40)

        # Train face button
        img9=Image.open(r"pictures\train.png")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.pic_img9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.pic_img9,cursor="hand2",command=self.train_data)
        b1.place(x=150,y=320,width=200,height=200)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=520,width=200,height=40)

        # photos face button
        img10=Image.open(r"pictures\image.jpg")
        img10=img10.resize((200,200),Image.ANTIALIAS)
        self.pic_img10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.pic_img10,cursor="hand2",command=self.open_img)
        b1.place(x=450,y=320,width=200,height=200)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=450,y=520,width=200,height=40)


        # Developer button
        img11=Image.open(r"pictures\Developer.jpg")
        img11=img11.resize((200,200),Image.ANTIALIAS)
        self.pic_img11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.pic_img11,cursor="hand2",command=self.developer)
        b1.place(x=750,y=320,width=200,height=200)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=750,y=520,width=200,height=40)


        # Exit button
        img12=Image.open(r"pictures\exit.png")
        img12=img12.resize((200,200),Image.ANTIALIAS)
        self.pic_img12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.pic_img12,cursor="hand2",command=self.exit)
        b1.place(x=1050,y=320,width=200,height=200)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1050,y=520,width=200,height=40)

    def open_img(self):
        os.startfile("data")

    def exit(self):
        self.exit=messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.exit >0:
            self.root.destroy()
        else:
            return





    #_____________function button________________
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

        






if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()

    