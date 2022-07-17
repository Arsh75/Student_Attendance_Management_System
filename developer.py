from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2



class Developer:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1360x700+0+0")
        self.root.title("Face Recognition system")
        self.root.wm_iconbitmap("face.ico")
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",30,"bold"),bg="white",fg="green" )
        title_lbl.place(x=0,y=0,width=1360,height=45)

        left_top1=Image.open(r"pictures\deve.jpg")
        left_top1=left_top1.resize((1350,650),Image.ANTIALIAS)
        self.pic_img_top1=ImageTk.PhotoImage(left_top1)

        f_lbl=Label(self.root,image=self.pic_img_top1)
        f_lbl.place(x=5,y=45,width=1350,height=650)
     
        #Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=800,y=0,width=500,height=600)

        img_top1=Image.open(r"pictures\front.png")
        img_top1=img_top1.resize((250,200),Image.ANTIALIAS)
        self.img_top1=ImageTk.PhotoImage(img_top1)

        f_lbl1=Label(main_frame,image=self.img_top1)
        f_lbl1.place(x=250,y=0,width=250,height=200)

        #Developer
        dep_label=Label(main_frame,text="Arshad Khan \nFront-end Development",font=("times new roman",16,"bold"),bg="white",fg="red")
        dep_label.place(x=0,y=60)
        dep_label1=Label(main_frame,text="Mohammad Hammmad\n back-end Development",font=("times new roman",16,"bold"),bg="white",fg="orange")
        dep_label1.place(x=270,y=250)
        dep_label2=Label(main_frame,text="Anas Farooqui\n Database Management",font=("times new roman",16,"bold"),bg="white",fg="purple")
        dep_label2.place(x=0,y=480)


        dep_label1=Label(main_frame,text="",font=("",20,"bold"),bg="white",fg="blue")
        dep_label1.place(x=0,y=40)

        img2=Image.open(r"pictures\back.png")
        img2=img2.resize((250,200),Image.ANTIALIAS)
        self.pic_img2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.pic_img2)
        f_lbl.place(x=0,y=200,width=250,height=200)

        dep_label2=Label(main_frame,text="",font=("",20,"bold"),bg="white",fg="blue")
        dep_label2.place(x=0,y=40)

        img3=Image.open(r"pictures\data.png")
        img3=img3.resize((250,200),Image.ANTIALIAS)
        self.pic_img3=ImageTk.PhotoImage(img3)

        f_lbl=Label(main_frame,image=self.pic_img3)
        f_lbl.place(x=250,y=400,width=250,height=200)




if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
