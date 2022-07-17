from os import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1360x700+0+0")
        self.root.title("Face Recognition system")
        self.root.wm_iconbitmap("face.ico")


        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",30,"bold"),bg="gray",fg="yellow" )
        title_lbl.place(x=0,y=0,width=1360,height=45)

        left_top1=Image.open(r"E:\Face recogniton project\pictures\train_5.jpeg")
        left_top1=left_top1.resize((450,210),Image.ANTIALIAS)
        self.pic_img_top1=ImageTk.PhotoImage(left_top1)

        f_lbl=Label(self.root,image=self.pic_img_top1)
        f_lbl.place(x=0,y=45,width=450,height=210)

        left_top2=Image.open(r"E:\Face recogniton project\pictures\face_5.jpg")
        left_top2=left_top2.resize((450,210),Image.ANTIALIAS)
        self.pic_img_top2=ImageTk.PhotoImage(left_top2)

        f_lbl=Label(self.root,image=self.pic_img_top2)
        f_lbl.place(x=455,y=45,width=450,height=210)

        left_top3=Image.open(r"E:\Face recogniton project\pictures\student3.gif")
        left_top3=left_top3.resize((455,210),Image.ANTIALIAS)
        self.pic_img_top3=ImageTk.PhotoImage(left_top3)

        f_lbl=Label(self.root,image=self.pic_img_top3)
        f_lbl.place(x=905,y=45,width=455,height=210)

        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",35,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=255,width=1360,height=60)

        img_bottom=Image.open(r"E:\Face recogniton project\pictures\dataset.jpg")
        img_bottom=img_bottom.resize((1360,440),Image.ANTIALIAS)
        self.pic_img_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.pic_img_bottom)
        f_lbl.place(x=0,y=315,width=1360,height=440)


    def train_classifier(self):
        data_dir=("data")
        path=[ os.path.join(data_dir,file) for file in os.listdir(data_dir) ]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #covert gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        # ============= Train the classifier===============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data Set Completed !",parent=self.root)

           
        

        




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()