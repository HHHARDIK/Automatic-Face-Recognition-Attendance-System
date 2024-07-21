# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:09:36 2024

@author: hardi
"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)

def create_student(sid, name, age):
    cursor = mydb.cursor()
    sql = "INSERT INTO students (sid, name, age) VALUES (%s, %s, %s)"
    val = (sid, name, age)
    cursor.execute(sql, val)
    mydb.commit()
    print("Student record inserted successfully")

def read_students():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    for row in result:
        print(row)

def update_student(sid, name, age):
    cursor = mydb.cursor()
    sql = "UPDATE students SET name = %s, age = %s WHERE sid = %s"
    val = (name, age, sid)
    cursor.execute(sql, val)
    mydb.commit()
    print("Student record updated successfully")

def delete_student(sid):
    cursor = mydb.cursor()
    sql = "DELETE FROM students WHERE sid = %s"
    val = (sid,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Student record deleted successfully")

while True:
    print("*********************************** CRUD DATABASE OPERATIONS *******************************\n")
    print("1.Create\n2.Read\n3.Update\n4.Delete\n5.ExitEnter operation to perform : ")
    ch=int(input())
    count=0
    if(ch==1):
        count+=1
        name=input("Enter Name : ")
        age=int(input("Enter Age : "))
        create_student(count,name, age)
        print("Record inserted")
    if(ch==2):
        read_students()
    if(ch==3):
        sid=int(input("Enter Id to update : "))
        name=input("Enter Name : ")
        age=int(input("Enter Age : "))
        update_student(sid, name, age)
        print("Records updated")
    if(ch==4):
        sid=int(input("Enter Id to delete : "))
        delete_student(sid)
    if(ch==5):
        break;


mydb.close()
