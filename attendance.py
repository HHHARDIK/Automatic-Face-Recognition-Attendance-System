from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
#  C:/Python310/python.exe c:/Users/hardi/Desktop/AFRAS/student.py
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ================== variables=======================================
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()

        title_lbl=Label(self.root,text="STUDENT ATTENDANCE SYSTEM",font=('arial',30,'bold'),fg='white',bg="black")
        title_lbl.place(x=0,y=0,width=1530,height=60)

        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=15,y=70,width=1500,height=800)

        #left label frame
        left_frame=LabelFrame(main_frame,text="Attendance Information",labelanchor='n',bd=2,bg="white",relief=RIDGE,font=('ariel',15,'bold'))
        left_frame.place(x=10,y=10,width=700,height=680)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=10,y=10,width=675,height=800)


        # labels and entry

        attendanceID_label=Label(left_inside_frame,text="Student ID :",font=('ariel',15,'bold'),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10)

        attendanceID_entry=ttk.Entry(left_inside_frame,font=('ariel',12),textvariable=self.var_attend_id,width=18)
        attendanceID_entry.grid(row=0,column=1,padx=10,sticky=W)

        rollLabel=Label(left_inside_frame,text="Roll :",font=('ariel',15,'bold'),bg="white")
        rollLabel.grid(row=1,column=0,padx=10)

        atten_roll=ttk.Entry(left_inside_frame,font=('ariel',12),textvariable=self.var_attend_roll,width=18)
        atten_roll.grid(row=1,column=1,padx=10,sticky=W)

        nameLabel=Label(left_inside_frame,text="Name :",font=('ariel',15,'bold'),bg="white")
        nameLabel.grid(row=1,column=2,padx=10)

        atten_name=ttk.Entry(left_inside_frame,font=('ariel',12),textvariable=self.var_attend_name,width=18)
        atten_name.grid(row=1,column=3,padx=10,sticky=W)

        depLabel=Label(left_inside_frame,text=" Department :",font=('ariel',15,'bold'),bg="white")
        depLabel.grid(row=2,column=0,padx=10)

        atten_dep=ttk.Entry(left_inside_frame,font=('ariel',12),textvariable=self.var_attend_dep,width=18)
        atten_dep.grid(row=2,column=1,padx=10,sticky=W)

        dateLabel=Label(left_inside_frame,text="Date :",font=('ariel',15,'bold'),bg="white")
        dateLabel.grid(row=2,column=2,padx=10)

        atten_date=ttk.Entry(left_inside_frame,font=('ariel',12),textvariable=self.var_attend_date,width=18)
        atten_date.grid(row=2,column=3,padx=10,sticky=W)

        attendanceLabel=Label(left_inside_frame,text="Attendance Status :",font=('ariel',15,'bold'),bg="white")
        attendanceLabel.grid(row=3,column=0,padx=10)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_attend_attendance,state="readonly")
        self.atten_status["values"]=["Status","Present","Absent"]
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        # ----------------------------------------------- buttons----------------------------------
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=674,height=45)

        savebtn=Button(btn_frame,text="Import csv",command=self.importCsv,width=14,font=('ariel',15))
        savebtn.grid(row=0,column=0)

        updatebtn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=14,font=('ariel',15))
        updatebtn.grid(row=0,column=1)

        delbtn=Button(btn_frame,text="Update",width=14,font=('ariel',15))
        delbtn.grid(row=0,column=2)

        rstbtn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=('ariel',15))
        rstbtn.grid(row=0,column=3)

        # right label Frame
        right_frame=LabelFrame(main_frame,text="Attendance Details",labelanchor='n',bd=2,bg="white",relief=RIDGE,font=('ariel',15,'bold'))
        right_frame.place(x=730,y=10,width=700,height=680)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=680,height=525)

        # ========== scroll bar table ======================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
                        
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    # ============================ fetch data ================================================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    # ======================= import csv=============================
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #=========================== export csv ==================
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("NO DATA !!","No Data Found")
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data exportes to "+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])


    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")

if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
