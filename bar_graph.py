from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Bargraph:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # Header Image
        img = Image.open(r"C:\Users\hp\Documents\Smart_Attendance_System\Images_GUI\banner.jpg")
        img = img.resize((1366, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # Background Image
        bg1 = Image.open(r"C:\Users\hp\Documents\Smart_Attendance_System\Images_GUI\bg3.jpg")
        bg1 = bg1.resize((1366, 768), Image.Resampling.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # Title
        title_lb1 = Label(bg_img, text="Visualize Attendance Report", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Back Button
        back_btn = Button(bg_img, text="Back", font=("times new roman", 12, "bold"), bg="red", fg="white", command=self.back_button)
        back_btn.place(x=1200, y=5, width=80, height=30)

        # Date Entry
        self.date_var = StringVar()
        date_label = Label(bg_img, text="Enter Date (YYYY-MM-DD):", font=("times new roman", 14, "bold"), bg="white")
        date_label.place(x=50, y=100)
        self.date_entry = Entry(bg_img, textvariable=self.date_var, font=("times new roman", 14))
        self.date_entry.place(x=300, y=100, width=200)

        # Show Graph Button
        show_btn = Button(bg_img, text="Show Graph", font=("times new roman", 14, "bold"), bg="green", fg="white", command=self.show_bargraph)
        show_btn.place(x=520, y=98, width=150, height=35)

    def back_button(self):
        from attendance import Attendance
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def show_bargraph(self):
        selected_date = self.date_var.get()
        if not selected_date:
            messagebox.showerror("Error", "Please enter a date.")
            return

        try:
            conn = mysql.connector.connect(username='root', password='Jyoti@1234', host='localhost', database='face_recognition', port=3306)
            cursor = conn.cursor()
            
            # Query to get all students with their attendance status
            query = """
                SELECT s.Name, COALESCE(a.atten_status, 'Absent') AS status
                FROM student s
                LEFT JOIN attendance a ON s.Student_ID = a.Student_ID AND a.atten_date = %s
            """
            cursor.execute(query, (selected_date,))
            data = cursor.fetchall()

            conn.close()
            
            # Process data for visualization
            names = []
            attendance_counts = []
            
            for row in data:
                names.append(row[0])
                attendance_counts.append(1 if row[1] == "Present" else 0)
            
            # Plot Bar Graph
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.bar(names, attendance_counts, color=['green' if count == 1 else 'red' for count in attendance_counts])
            ax.set_xlabel("Students")
            ax.set_ylabel("Attendance Status")
            ax.set_title(f"Attendance Report for {selected_date}")
            ax.set_xticklabels(names, rotation=45, ha='right')
            ax.set_yticks([0, 1])
            ax.set_yticklabels(["Absent", "Present"])

            # Embed Graph in Tkinter
            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas.draw()
            canvas.get_tk_widget().place(x=50, y=200, width=1000, height=500)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error connecting to database: {err}")

if __name__ == "__main__":
    root = Tk()
    obj = Bargraph(root)
    root.mainloop()
