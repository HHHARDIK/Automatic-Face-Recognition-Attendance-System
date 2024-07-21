from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

#  C:/Python310/python.exe c:/Users/hardi/Desktop/AFRAS/student.py
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        # *************************Variables************************
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
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
             
        # bg image
        bgimg=Image.open(r"C:\Users\hardi\Desktop\AFRAS\images\bg4.jpg")
        bgimg=bgimg.resize((1530,790),Image.ANTIALIAS)
        self.bgimage=ImageTk.PhotoImage(bgimg)

        bg_img=Label(self.root,image=self.bgimage)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=('arial',30,'bold'),fg='white',bg="black")
        title_lbl.place(x=0,y=0,width=1530,height=60)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=15,y=70,width=1500,height=800)

        # left label Frame
        left_frame=LabelFrame(main_frame,text="Student Information",labelanchor='n',bd=2,bg="white",relief=RIDGE,font=('ariel',15,'bold'))
        left_frame.place(x=10,y=10,width=700,height=680)

        img=Image.open(r"C:\Users\hardi\Desktop\AFRAS\images\students.jpg")
        img=img.resize((720,130),Image.ANTIALIAS)
        self.imgg=ImageTk.PhotoImage(img)

        f_lbl=Label(left_frame,image=self.imgg)
        f_lbl.place(x=5,y=0,width=690,height=130)

        # current course
        current_course_frame=LabelFrame(left_frame,text="Current Course Information",labelanchor='n',bd=2,bg="white",relief=RIDGE,font=('ariel',15,'bold'))
        current_course_frame.place(x=10,y=135,width=680,height=150)


        # department combo box
        dep_label=Label(current_course_frame,text="Department :",font=('ariel',15,'bold'),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=('ariel',12,'bold'),width=17,state='readonly')
        dep_combo["values"]=("Select Department","CSE","Civil","Mechanical","Electronics")
        dep_combo.current(0)

        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # course combo box
        course_label=Label(current_course_frame,text="Course :",font=('ariel',15,'bold'),bg="white")
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=('ariel',12,'bold'),width=17,state='readonly')
        course_combo["values"]=("Select Course","M.C.A.","B.Tech.","M.Tech.")
        course_combo.current(0)

        course_combo.grid(row=0,column=3,padx=2,pady=10)

         # year combo box
        year_label=Label(current_course_frame,text="Year :",font=('ariel',15,'bold'),bg="white")
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=('ariel',12,'bold'),width=17,state='readonly')
        year_combo["values"]=("Select Year","2023-24","2022-23","2021-22")
        year_combo.current(0)

        year_combo.grid(row=1,column=1,padx=2,pady=10)

         # semester combo box
        sem_label=Label(current_course_frame,text="Semester :",font=('ariel',15,'bold'),bg="white")
        sem_label.grid(row=1,column=2,padx=10)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=('ariel',12,'bold'),width=17,state='readonly')
        sem_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)

        sem_combo.grid(row=1,column=3,padx=2,pady=10)


        # student course
        student_frame=LabelFrame(left_frame,text="Student Details",labelanchor='n',bd=2,bg="white",relief=RIDGE,font=('ariel',15,'bold'))
        student_frame.place(x=10,y=335,width=680,height=300)

        # student id
        sid_label=Label(student_frame,text="Student ID :",font=('ariel',15,'bold'),bg="white")
        sid_label.grid(row=0,column=0,padx=10)

        sid_entry=ttk.Entry(student_frame,textvariable=self.var_std_id,font=('ariel',12),width=18)
        sid_entry.grid(row=0,column=1,padx=10,sticky=W)

        # student name
        sname_label=Label(student_frame,text="Student Name :",font=('ariel',15,'bold'),bg="white")
        sname_label.grid(row=0,column=2,padx=10)

        sname_entry=ttk.Entry(student_frame,textvariable=self.var_std_name,font=('ariel',12),width=18)
        sname_entry.grid(row=0,column=3,padx=10,sticky=W)

        # roll no.
        sroll_label=Label(student_frame,text="Roll No. :",font=('ariel',15,'bold'),bg="white")
        sroll_label.grid(row=1,column=0,padx=10)

        sroll_entry=ttk.Entry(student_frame,textvariable=self.var_roll,font=('ariel',12),width=18)
        sroll_entry.grid(row=1,column=1,padx=10,sticky=W)

        # student Gender
        gen_label=Label(student_frame,text=" Gender :",font=('ariel',15,'bold'),bg="white")
        gen_label.grid(row=1,column=2,padx=10)

        # gen_entry=ttk.Entry(student_frame,textvariable=self.var_gender,font=('ariel',12),width=18)
        # gen_entry.grid(row=1,column=3,padx=10,sticky=W)

        gender_combo=ttk.Combobox(student_frame,textvariable=self.var_gender,font=('ariel',12,'bold'),width=17,state='readonly')
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=10,sticky=W)

        # class division
        div_label=Label(student_frame,text="Division :",font=('ariel',15,'bold'),bg="white")
        div_label.grid(row=2,column=0,padx=10)

        div_entry=ttk.Entry(student_frame,textvariable=self.var_div,font=('ariel',12),width=18)
        div_entry.grid(row=2,column=1,padx=10,sticky=W)


        # D.O.B
        dob_label=Label(student_frame,text=" D.O.B. :",font=('ariel',15,'bold'),bg="white")
        dob_label.grid(row=2,column=2,padx=10)

        dob_entry=ttk.Entry(student_frame,textvariable=self.var_dob,font=('ariel',12),width=18)
        dob_entry.grid(row=2,column=3,padx=10,sticky=W)


        # email id
        email_label=Label(student_frame,text="Email ID :",font=('ariel',15,'bold'),bg="white")
        email_label.grid(row=3,column=0,padx=10)

        email_entry=ttk.Entry(student_frame,textvariable=self.var_email,font=('ariel',12),width=18)
        email_entry.grid(row=3,column=1,padx=10,sticky=W)


        # Phone No.
        phn_label=Label(student_frame,text="Phone No. :",font=('ariel',15,'bold'),bg="white")
        phn_label.grid(row=3,column=2,padx=10)

        phn_entry=ttk.Entry(student_frame,textvariable=self.var_phone,font=('ariel',12),width=18)
        phn_entry.grid(row=3,column=3,padx=10,sticky=W)

        # Address
        addr_label=Label(student_frame,text="Address :",font=('ariel',15,'bold'),bg="white")
        addr_label.grid(row=4,column=0,padx=10)

        addr_entry=ttk.Entry(student_frame,textvariable=self.var_address,font=('ariel',12),width=18)
        addr_entry.grid(row=4,column=1,padx=10,sticky=W)

        # Teacher
        teacher_label=Label(student_frame,text="Teacher :",font=('ariel',15,'bold'),bg="white")
        teacher_label.grid(row=4,column=2,padx=10)

        teacher_entry=ttk.Entry(student_frame,textvariable=self.var_teacher,font=('ariel',12),width=18)
        teacher_entry.grid(row=4,column=3,padx=10,sticky=W)

       
# ----------------------------------------------- radio buttons----------------------------------
        
        style = ttk.Style()
        style.configure("White.TRadiobutton", background="white")
        
        self.var_radio1=StringVar()
        rb1=ttk.Radiobutton(student_frame,text="Take Photo Sample",variable=self.var_radio1, value="Yes", style="White.TRadiobutton")
        rb1.grid(row=5,column=0)

        # self.var_radio2=StringVar()
        rb2=ttk.Radiobutton(student_frame,text="No Photo Sample",variable=self.var_radio1, value="No", style="White.TRadiobutton")
        rb2.grid(row=5,column=1)

        # ----------------------------------------------- buttons----------------------------------
        btn_frame=Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=674,height=85)

        savebtn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=('ariel',15))
        savebtn.grid(row=0,column=0)

        updatebtn=Button(btn_frame,text="Update",command=self.update_data,width=14,font=('ariel',15))
        updatebtn.grid(row=0,column=1)

        delbtn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=('ariel',15))
        delbtn.grid(row=0,column=2)

        rstbtn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=('ariel',15))
        rstbtn.grid(row=0,column=3)

        take_pic_btn=Button(btn_frame,text="Take Photo Sample",command=self.generate_dataset,width=30,font=('ariel',15))
        take_pic_btn.grid(row=1,column=0, columnspan=2)

        update_pic_btn=Button(btn_frame,text="Update Photo Sample",width=30,font=('ariel',15))
        update_pic_btn.grid(row=1,column=2, columnspan=2)





        # right label Frame
        right_frame=LabelFrame(main_frame,text="Search System",labelanchor='n',bd=2,bg="white",relief=RIDGE,font=('ariel',15,'bold'))
        right_frame.place(x=730,y=10,width=700,height=680)

        search_frame=LabelFrame(right_frame,labelanchor='n',bd=2,bg="white",relief=RIDGE,font=('ariel',15,'bold'))
        search_frame.place(x=0,y=5,width=695,height=60)

        searchby_label=Label(search_frame,text="Search By :",font=('ariel',15,'bold'),bg="white")
        searchby_label.grid(row=0,column=0,padx=10,pady=17)

        # search by combo box
        sby_combo=ttk.Combobox(search_frame,font=('ariel',10,'bold'),width=13,state='readonly')
        sby_combo["values"]=("Select","Roll_no","Phone_no")
        sby_combo.current(0)

        sby_combo.grid(row=0,column=1,padx=2,pady=17)

        sby_entry=ttk.Entry(search_frame,font=('ariel',12),width=18)
        sby_entry.grid(row=0,column=2,padx=2,sticky=W,pady=17)

        searchbtn=Button(search_frame,text="Search",width=10,font=('ariel'))
        searchbtn.grid(row=0,column=3,padx=15)

        showallbtn=Button(search_frame,text="Show All",width=10,font=('ariel'))
        showallbtn.grid(row=0,column=4)


        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=80,width=690,height=565)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text= "Year")
        self.student_table.heading("sem", text = "Semester")
        self.student_table.heading("id",text="Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=True)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        # ---------------------------------------------function declaration-------------------------------------------------
    def add_data(self):
        if(self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()==""):
            messagebox.showerror("ERROR!", "All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
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
                    self.var_radio1.get()
                ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Data added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

        
    # ============================================= fetch data=========================================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select  * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('', 'end', values=i)
            conn.commit()
        conn.close()

    # ================== ========================= get cursor================================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content['values']
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    # ============================================ update function ======================================
    def update_data(self):
        if(self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()==""):
            messagebox.showerror("ERROR!", "All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update details",parent=self.root)
                if Update>0 :
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                      
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(), 
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()

                                      
                                      
                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updtaed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    # ========================== delete function ==================================
                
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("ERROR","Student id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="DELETE FROM student WHERE Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deletedd student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    # ============================================ reset function ======================================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ generate dataset / take photo sample ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def generate_dataset(self):
        if(self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()==""):
            messagebox.showerror("ERROR!", "All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE student SET Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                      
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(), 
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id+1

                                      
                                      
                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            

        # =========== Load predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if ret:
                        img_id+=1
                    
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)
                    
                













if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
