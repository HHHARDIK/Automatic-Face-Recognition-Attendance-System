from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
import tkinter
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

#C:/Python310/python.exe c:/Users/hardi/Desktop/AFRAS/main.py
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        # bg image
        bgimg=Image.open(r"images\bg4.jpg")
        bgimg=bgimg.resize((1530,790),Image.ANTIALIAS)
        self.bgimage=ImageTk.PhotoImage(bgimg)

        bg_img=Label(self.root,image=self.bgimage)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lbl=Label(bg_img,text="AUTOMATED FACE RECOGNITION SYSTEM",font=('arial',30,'bold'),fg='white',bg="black")
        title_lbl.place(x=0,y=0,width=1530,height=60)

        #student details button
        b1=Image.open(r"images\student_details.png")
        b1=b1.resize((220,220),Image.ANTIALIAS)
        self.btn1=ImageTk.PhotoImage(b1)

        bt1=Button(bg_img,image=self.btn1,command=self.student_details,cursor="hand2")
        bt1.place(x=200,y=140,width=220,height=220)

        bt1_1=Button(bg_img,text="Student Details",cursor="hand2",command=self.student_details,font=('arial',15,'bold'),fg='black',bg="white")
        bt1_1.place(x=200,y=340,width=220,height=30)

        # Face recognition button
        b2=Image.open(r"images\face_detection.png")
        b2=b2.resize((220,220),Image.ANTIALIAS)
        self.btn2=ImageTk.PhotoImage(b2)

        bt2=Button(bg_img,image=self.btn2,cursor="hand2",command=self.face_data)
        bt2.place(x=600,y=140,width=220,height=220)

        bt2_2=Button(bg_img,text="Detect Face",cursor="hand2",command=self.face_data,font=('arial',15,'bold'),fg='black',bg="white")
        bt2_2.place(x=600,y=340,width=220,height=30)


        # Attendance button
        b3=Image.open(r"images\attendance.png")
        b3=b3.resize((220,220),Image.ANTIALIAS)
        self.btn3=ImageTk.PhotoImage(b3)

        bt3=Button(bg_img,image=self.btn3,cursor="hand2",command=self.attendance_data)
        bt3.place(x=1000,y=140,width=220,height=220)

        bt3_3=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=('arial',15,'bold'),fg='black',bg="white")
        bt3_3.place(x=1000,y=340,width=220,height=30)


        # Train data button
        b4=Image.open(r"images\train_data.png")
        b4=b4.resize((220,220),Image.ANTIALIAS)
        self.btn4=ImageTk.PhotoImage(b4)

        bt4=Button(bg_img,image=self.btn4,cursor="hand2",command=self.train_data)
        bt4.place(x=200,y=500,width=220,height=220)

        bt4_4=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=('arial',15,'bold'),fg='black',bg="white")
        bt4_4.place(x=200,y=700,width=220,height=30)

        # Photos button
        b5=Image.open(r"images\photos.jpg")
        b5=b5.resize((220,220),Image.ANTIALIAS)
        self.btn5=ImageTk.PhotoImage(b5)

        bt5=Button(bg_img,image=self.btn5,cursor="hand2",command=self.open_img)
        bt5.place(x=600,y=500,width=220,height=220)

        bt5_5=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=('arial',15,'bold'),fg='black',bg="white")
        bt5_5.place(x=600,y=700,width=220,height=30)


        # Exit button
        b6=Image.open(r"images\exit.png")
        b6=b6.resize((220,220),Image.ANTIALIAS)
        self.btn6=ImageTk.PhotoImage(b6)

        bt6=Button(bg_img,image=self.btn6,cursor="hand2",command=self.iExit)
        bt6.place(x=1000,y=500,width=220,height=220)

        bt6_6=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=('arial',15,'bold'),fg='black',bg="white")
        bt6_6.place(x=1000,y=700,width=220,height=30)


    def open_img(self):
        os.startfile("data")


# ======================== Function buttons ==================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit this project ?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

















if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
