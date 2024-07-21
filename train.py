from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

#  C:/Python310/python.exe c:/Users/hardi/Desktop/AFRAS/train.py
class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        rstbtn=Button(self.root,text="TRAIN",command=self.train_classifier,font=('ariel',15))
        # rstbtn.grid(row=0,column=3)
        rstbtn.place(x=650,y=180,width=220,height=120)





    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')  # convert to gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])  # extract the person number from the image file name
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # ================================= Train the classifier =========================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!!")









if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    
    root.mainloop()
