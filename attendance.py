# import re
import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
#from dotenv import load_dotenv
import mysql.connector
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
from tkinter import filedialog
from bar_graph import Bargraph

#Global variable for importCsv Function 
mydata=[]
class Attendance:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Attendance Pannel")

        #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\hp\\Documents\Smart_Attendance_System\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\hp\\Documents\Smart_Attendance_System\Images_GUI\bg2.jpg")
        bg1=bg1.resize((1366,768),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Attendance Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)
        
        
        # Back Button
        back_btn = Button(bg_img, text="Back", font=("Verdana", 12, "bold"), bg="red", fg="white", command=self.back_button)
        back_btn.place(x=1200, y=5, width=80, height=30)

        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=55,width=1355,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=660,height=480)

        

        # ==================================Text boxes and Combo Boxes====================

        #Student id
        studentId_label = Label(left_frame,text="Std-ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(left_frame,textvariable=self.var_id,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Student Roll
        student_roll_label = Label(left_frame,text="Roll.No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(left_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Studnet Name
        student_name_label = Label(left_frame,text="Std-Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(left_frame,textvariable=self.var_name,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Department
        dep_label = Label(left_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        dep_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        dep_entry = ttk.Entry(left_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"))
        dep_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        
        #Year 
        year_label = Label(left_frame,text="Year:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        year_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        year_entry = ttk.Entry(left_frame,textvariable=self.var_year,width=15,font=("verdana",12,"bold"))
        year_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)
        
        #Semester
        sem_label = Label(left_frame,text="Semester:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        sem_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        year_entry = ttk.Entry(left_frame,textvariable=self.var_sem,width=15,font=("verdana",12,"bold"))
        year_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)
        
        
        #time
        time_label = Label(left_frame,text="Time:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        time_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(left_frame,textvariable=self.var_time,width=15,font=("verdana",12,"bold"))
        time_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(left_frame,text="Date:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        date_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_frame,textvariable=self.var_date,width=15,font=("verdana",12,"bold"))
        date_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        #Attendance
        student_attend_label = Label(left_frame,text="Attend-status:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_attend_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        attend_combo=ttk.Combobox(left_frame,textvariable=self.var_attend,width=13,font=("verdana",12,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=4,column=1,padx=5,pady=5,sticky=W)
    

        # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=390,width=635,height=60)

        #Improt button
        save_btn=Button(btn_frame,command=self.bargraph,text="View Graph",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)

        # #Exprot button
        # update_btn=Button(btn_frame,command="self.exportCsv",text=" can_add",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        # update_btn.grid(row=0,column=1,padx=6,pady=8,sticky=W)

        #Update button
        del_btn=Button(btn_frame,command=self.update_data,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)



        # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=680,y=10,width=660,height=480)


        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=635,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("ID","Roll_No","Name","Department","Year","Semester","Time","Date","Attend-status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("ID",text="Std-ID")
        self.attendanceReport.heading("Roll_No",text="Roll.No")
        self.attendanceReport.heading("Name",text="Std-Name")
        self.attendanceReport.heading("Department",text="Department")
        self.attendanceReport.heading("Year",text="Year")
        self.attendanceReport.heading("Semester",text="Semester")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attend-status",text="Attend-status")
        self.attendanceReport["show"]="headings"

        # Set Width of Columns 
        self.attendanceReport.column("ID",width=100)
        self.attendanceReport.column("Roll_No",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Department",width=120)
        self.attendanceReport.column("Year",width=80)
        self.attendanceReport.column("Semester",width=100)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Attend-status",width=100)

        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    # =================================update for mysql button================
    #Search button
        del_btn=Button(right_frame,command="#",text="Search",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=1,padx=6,pady=10,sticky=W)
    #Delete button
        del_btn=Button(right_frame,command=self.delete_data,text="Delete",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)
        
        
            # ===========================Update Attendance Status===========
    def update_data(self):
        selected_item = self.attendanceReport.focus()
        if not selected_item:
            messagebox.showerror("Error", "No record selected to update")
            return
        
        values = self.attendanceReport.item(selected_item, "values")
        if not values:
            messagebox.showerror("Error", "Invalid selection")
            return
        
        student_id = values[0]  # Assuming Student_ID is the first column
        new_status = self.var_attend.get()
        
        conn = mysql.connector.connect(username='root', password='Jyoti@1234', host='localhost', database='face_recognition', port=3306)
        mycursor = conn.cursor()
        
        # Update attendance status only
        mycursor.execute("""
            INSERT INTO attendance (Student_ID, atten_status)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE atten_status = VALUES(atten_status)
        """, (student_id, new_status))
        
        conn.commit()
        conn.close()
        
        self.fetch_data()  # Refresh the data after update
        messagebox.showinfo("Success", "Attendance status updated successfully")
            
            
    
    # =============================Delete Attendance form my sql============================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='Jyoti@1234',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from attendance where Student_ID=%s"
                    val=(self.var_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
                
                # ===========================Fetch Data from Database===========
    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='Jyoti@1234', host='localhost', database='face_recognition', port=3306)
        mycursor = conn.cursor()
        
        # Fetch present students from attendance table with student details
        mycursor.execute("""
            SELECT s.Student_ID, s.Roll_No, s.Name, s.Department, s.Year, s.Semester, a.atten_time, a.atten_date, a.atten_status
            FROM student s
            INNER JOIN attendance a ON s.Student_ID = a.Student_ID
            WHERE a.atten_status = 'Present'
        """)
        present_data = mycursor.fetchall()
        
        # Fetch students who are not in the attendance table or do not have 'Present' status
        mycursor.execute("""
            SELECT s.Student_ID, s.Roll_No, s.Name, s.Department, s.Year, s.Semester, NULL as atten_time, NULL as atten_date, 'Absent' as atten_status
            FROM student s
            LEFT JOIN attendance a ON s.Student_ID = a.Student_ID AND a.atten_status = 'Present'
            WHERE a.Student_ID IS NULL OR a.atten_status IS NULL OR a.atten_status != 'Present'
        """)
        absent_data = mycursor.fetchall()
        
        # Combine both datasets
        data = present_data + absent_data
        
        if len(data) != 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("", END, values=i)
            conn.commit()
        
        conn.close()


    #============================Reset Data======================
    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_year.set("")
        self.var_sem.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")

    # =========================Fetch Data Import data ===============

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport.delete(*self.attendanceReport.get_children())
        for i in rows:
            self.attendanceReport.insert("",END,values=i)
            print(i)
    


    #=============Cursor Function========================
    def get_cursor(self, event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]
        
        if data:
            self.var_id.set(data[0])
            self.var_roll.set(data[1])
            self.var_name.set(data[2])
            self.var_dep.set(data[3])
            self.var_year.set(data[4])
            self.var_sem.set(data[5])
            self.var_time.set(data[6])
            self.var_date.set(data[7])
            self.var_attend.set(data[8])
            
            
            
    def bargraph(self):
        self.new_window=Toplevel(self.root)
        self.app=Bargraph(self.new_window)        

    
    

    #function for back button
    def back_button(self):
      from main import Face_Recognition_System
      self.new_window=Toplevel(self.root)
      self.app=Face_Recognition_System(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()