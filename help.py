from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2



class Help:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1360x700+0+0")
        self.root.title("Face Recognition system")
        self.root.wm_iconbitmap("face.ico")
        
        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",30,"bold"),bg="white",fg="blue" )
        title_lbl.place(x=0,y=0,width=1360,height=45)

        left_top1=Image.open(r"pictures\help.jpg")
        left_top1=left_top1.resize((1350,650),Image.ANTIALIAS)
        self.pic_img_top1=ImageTk.PhotoImage(left_top1)

        f_lbl=Label(self.root,image=self.pic_img_top1)
        f_lbl.place(x=5,y=45,width=1350,height=650)

        dep_label=Label(f_lbl,text="Email:attendance245@gmail.com ",font=("times new roman",20,"bold"),bg="white",fg="blue")
        dep_label.place(x=520,y=80)



if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()