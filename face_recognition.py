from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from  datetime import datetime
from time import strftime
import cv2
import csv
import os
import numpy as np

#  C:/Python310/python.exe c:/Users/hardi/Desktop/AFRAS/train.py
class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=('arial', 30, 'bold'), fg='white', bg="black")
        title_lbl.place(x=0, y=0, width=1530, height=60)

        rstbtn = Button(self.root, text="Start Recognition", command=self.face_recog, width=55, height=7, font=('ariel', 15))
        rstbtn.place(x=650,y=180,width=220,height=220)
        # rstbtn.grid(row=0, column=3)


    # =========================================== attendenace ================================
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.strip().split(",")  
                name_list.append(entry)
            
           
            for ip in name_list:
                if(n in ip):
                    return  
            
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
            
        


    # ============================================= face recognition -=====================================
        
    def face_recog(self):
        def draw_boundry(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            if img is not None:
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)
                for (x, y, w, h) in features:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)
                    id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                    confidence = int(100 * (1 - predict/300))
                    conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                    my_cursor = conn.cursor()

                    my_cursor.execute("SELECT Name from student where Student_id="+str(id))
                    n = my_cursor.fetchone()
                    if n is not None:
                        n = n[0]
                    else:
                        n="unknown"

                    my_cursor.execute("SELECT Roll from student where Student_id="+str(id))
                    r = my_cursor.fetchone()
                    if r is not None:
                        r = "+".join(r)


                    my_cursor.execute("SELECT Dep from student where Student_id="+str(id))
                    d = my_cursor.fetchone()
                    if d is not None:
                        d = "+".join(d)

                    if confidence > 77:
                        cv2.putText(img, f"Roll :{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name :{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department :{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attendance(id, r, n, d)
                    else:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        cv2.putText(img, f"Unknown Face", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

        def recognize(img, clf, faceCascade):
            draw_boundry(img, faceCascade, 1.1, 10, ((0, 0, 255)), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read('classifier.xml')

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            if ret:  # Check if frame is captured successfully
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome to face Recognition", img)
            if cv2.waitKey(1) == 13:
                break

        video_cap.release()  # Release the video capture object
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
