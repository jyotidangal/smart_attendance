from sys import path 
from tkinter import *
from PIL import Image, ImageTk
import smtplib
import mysql.connector
import socket
import cv2
#from dotenv import load_dotenv
from time import strftime
from datetime import datetime,timedelta
from tkinter import messagebox
class Face_Recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Panel")

        # This part is image labels setting start 
        # first header image  
        img = Image.open(r"C:\Users\hp\Documents\Smart_Attendance_System\Images_GUI\banner.jpg")
        img = img.resize((1366, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # background image 
        bg1 = Image.open(r"C:\Users\hp\Documents\Smart_Attendance_System\Images_GUI\bg2.jpg")
        bg1 = bg1.resize((1366, 768), Image.Resampling.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # title section
        title_lb1 = Label(bg_img, text="Welcome to Face Recognition Panel", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)
        
        # Back Button
        back_btn = Button(bg_img, text="Back", font=("Verdana", 12, "bold"), bg="red", fg="white", command=self.back_button)
        back_btn.place(x=1200, y=5, width=80, height=30)

        # Create buttons below the section 
        std_img_btn = Image.open(r"C:\Users\hp\Documents\Smart_Attendance_System\Images_GUI\f_det.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.Resampling.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.face_recog, image=self.std_img1, cursor="hand2")
        std_b1.place(x=600, y=170, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.face_recog, text="Face Detector", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=600, y=350, width=180, height=45)
     
      # Function to check internet connection
    def check_internet(self):
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            return False

     
     
     # Function to send email
    def send_email(self,student_email, student_name):
        if not self.check_internet():
            messagebox.showerror("No internet connection. Email cannot be sent.")
            return
        try:
            server = smtplib.SMTP('smtp.gmail.com',587)  
            server.starttls()
            server.login("jdangal060@gmail.com", "cqyu uakw ilby ffeq")  
            subject = "Attendance Marked"
            body = f"Hello {student_name},\n\nYour attendance has been successfully marked as Present."
            message = f"Subject: {subject}\n\n{body}"
            
            server.sendmail("jdangal060@gmail.com", student_email, message)
            server.quit()
            messagebox.showinfo("Email sent to {student_email}")
        except Exception as e:
            messagebox.showerror(f"Error: {e}")
            
            
        # Attendance marking function
    def mark_attendance(self, student_id):
        conn = mysql.connector.connect(username='root', password='Jyoti@1234', host='localhost', database='face_recognition', port=3306)
        cursor = conn.cursor()

        now = datetime.now()
        atten_date = now.strftime("%Y-%m-%d")
        atten_time = now.strftime("%H:%M:%S")
        five_minutes_ago = (now - timedelta(minutes=5)).strftime("%H:%M:%S")

        # Check if the student was marked present in the last 5 minutes
        cursor.execute("""
            SELECT * FROM attendance 
            WHERE Student_ID = %s AND atten_date = %s AND atten_time >= %s
        """, (student_id, atten_date, five_minutes_ago))
        result = cursor.fetchone()

        if not result:
            # Insert attendance data into the database
            cursor.execute("INSERT INTO attendance (Student_ID, atten_time, atten_date, atten_status) VALUES (%s, %s, %s, %s)", (student_id, atten_time, atten_date, "Present"))
            conn.commit()

            # Fetch the student's email and name from the student table
            cursor.execute("SELECT name, email FROM student WHERE Student_ID = %s", (student_id,))
            student_data = cursor.fetchone()

            if student_data:
                student_name = student_data[0]
                student_email = student_data[1]
                # Send email notification to the student
                self.send_email(student_email, student_name)

        cursor.close()
        conn.close()

# ==================== Face Recognition ===================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                student_id, predict = clf.predict(gray_image[y:y + h, x:x + w])

                confidence = int((100 * (1 - predict / 300)))

                # Connect to MySQL database
                conn = mysql.connector.connect(username='root', password='Jyoti@1234', host='localhost', database='face_recognition', port=3306)
                cursor = conn.cursor()

                cursor.execute("SELECT Name, Roll_No FROM student WHERE Student_ID = %s", (student_id,))
                result = cursor.fetchone()
                
                cursor.close()
                conn.close()

                if result:
                    name, roll_no = result
                else:
                    name, roll_no, student_id = "Unknown", "Unknown", "Unknown"

                if confidence > 60 and student_id != "Unknown":
                    cv2.putText(img, f"Student_ID:{student_id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Name:{name}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Roll-No:{roll_no}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(student_id)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
                
                coord = [x, y, w, h]

            return coord

        # ====================== recognition part ====================== #
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap = cv2.VideoCapture(0)

        while True:
            ret, img = videoCap.read()
            if not ret:
                break  # Exit if the webcam doesn't capture frames

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Detector", img)

            # Wait for the Enter key to exit
            if cv2.waitKey(1) & 0xFF == 13:  # 13 is the Enter key
                break

        videoCap.release()
        cv2.destroyAllWindows()
        
    #Function for Back Button     
    def back_button(self):
      from main import Face_Recognition_System
      self.new_window=Toplevel(self.root)
      self.app=Face_Recognition_System(self.new_window)    

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
