import sqlite3
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as tkMessageBox


# ----- DEFINE CUSTOM FONTS ------
LARGE_FONT = ("Verdana Bold", 18)
MEDIUM_FONT = ("Verdana Bold", 12)
SMALL_FONT = ("Verdana", 8)


class instructor_frame:

    def __init__(self, window):

        # ---------------- Define Interface ----------------
        self.data = None
        self.row = None
        self.styles_data = []
        self.availability = []
        self.instructor_window = window
        self.instructor_window.title("DanceFeet - Instructor")
        self.instructor_window.geometry("1800x900+50+50")
        self.instructor_window.resizable(False, False)

        # ---------------- Create Variables for Students ----------------
        self.STD_ID = tkinter.StringVar()
        self.FIRSTNAME = tkinter.StringVar()
        self.HRATE = tkinter.StringVar()
        self.INSTRUCTOR = tkinter.StringVar()
        self.INSTRUCTOR_COMBO = tkinter.StringVar()
        self.STYLE = tkinter.StringVar()

        # ---------------- Create Variables for Instructors ----------------
        self.INS_ID = tkinter.StringVar()
        self.NAME_INS = tkinter.StringVar()
        self.GENDER_INS = tkinter.StringVar()
        self.STYLE_INS = tkinter.StringVar()
        self.TP_INS = tkinter.StringVar()
        self.HRATE_INS = tkinter.StringVar()
        self.AVAILABILITY_INS = tkinter.StringVar()
        self.PASSWORD_INS = tkinter.StringVar()
        self.STYLE1_INS = IntVar()
        self.STYLE2_INS = IntVar()
        self.STYLE3_INS = IntVar()
        self.STYLE4_INS = IntVar()
        self.DAY1_INS = IntVar()
        self.DAY2_INS = IntVar()
        self.DAY3_INS = IntVar()
        self.DAY4_INS = IntVar()
        self.DAY5_INS = IntVar()
        self.DAY6_INS = IntVar()
        self.DAY7_INS = IntVar()

        self.label = Label(window, text="ADMIN AREA", font=LARGE_FONT)
        self.label.pack(side=TOP, fill=X)

        # -------------- Create Top Frame ----------------
        self.Top = Frame(self.instructor_window, bd=4, relief=RIDGE)
        self.Top.pack(side=TOP)

        # -------------- Create Body top Frame ----------------
        self.BodyTop = Frame(self.instructor_window, bd=3, relief=RIDGE)
        self.BodyTop.place(x=5, y=148, width=400, height=500)

        # -------------- Create Body top Title Frame ----------------
        self.BodyTopTitle = Frame(self.instructor_window, bd=3, relief=RIDGE)
        self.BodyTopTitle.place(x=5, y=110, width=400, height=40)

        # -------------- Create Body bottom Frame ----------------
        self.BodyBottom = Frame(self.instructor_window, bd=3, relief=RIDGE)
        self.BodyBottom.place(x=5, y=580, width=400, height=340)
        
        # -------------- Create Right Frame ----------------
        self.Right = Frame(self.instructor_window, bd=3, relief=RIDGE)
        self.Right.place(x=404, y=110, width=1390, height=738)

        # -------------- Create Right Bottom Frame ----------------
        self.Right_bottom = Frame(self.instructor_window, bd=3, relief=RIDGE)
        self.Right_bottom.place(x=404, y=845, width=1390, height=50)

        # -------------- Student Table view ----------------
        self.tree_std = ttk.Treeview(self.BodyTop, columns=("id", "fname", "styles", "hrate", "instructor",), selectmode="extended", height=500)

        self.tree_std.heading('id', text="ID", anchor=W)
        self.tree_std.heading('fname', text="FirstName", anchor=W)
        self.tree_std.heading('styles', text="Styles", anchor=W)
        self.tree_std.heading('hrate', text="HourlyRate", anchor=W)
        self.tree_std.heading('instructor', text="Instructor", anchor=W)

        self.tree_std.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree_std.column('#1', stretch=NO, minwidth=0, width=25)
        self.tree_std.column('#2', stretch=NO, minwidth=0, width=90)
        self.tree_std.column('#3', stretch=NO, minwidth=0, width=90)
        self.tree_std.column('#4', stretch=YES, minwidth=0, width=90)
        self.tree_std.column('#5', stretch=YES, minwidth=0, width=90)
        self.tree_std.pack()
        self.tree_std.bind('<ButtonRelease-1>', self.OnSelected_STD)

        # -------------- Instructor Table view ----------------
        self.tree = ttk.Treeview(self.Right, columns=(
            "id", "name", "gender", "style", "mobile", "hrate", "availability", "password", "styles1", "styles2",
            "styles3", "styles4", "day1", "day2", "day3", "day4", "day5", "day6", "day7"), selectmode="extended",
                                  height=500)

        self.tree.heading('id', text="ID", anchor=W)
        self.tree.heading('name', text="Name", anchor=W)
        self.tree.heading('gender', text="Gender", anchor=W)
        self.tree.heading('style', text="Dancing Style", anchor=W)
        self.tree.heading('mobile', text="Mobile", anchor=W)
        self.tree.heading('hrate', text="HourlyRate", anchor=W)
        self.tree.heading('availability', text="Availability", anchor=W)
        self.tree.heading('password', text="Password", anchor=W)
        self.tree.heading('styles1', text="Waltz", anchor=W)
        self.tree.heading('styles2', text="Jive", anchor=W)
        self.tree.heading('styles3', text="ChaCha", anchor=W)
        self.tree.heading('styles4', text="Samba", anchor=W)
        self.tree.heading('day1', text="Sunday", anchor=W)
        self.tree.heading('day2', text="Monday", anchor=W)
        self.tree.heading('day3', text="Tuesday", anchor=W)
        self.tree.heading('day4', text="Wednesday", anchor=W)
        self.tree.heading('day5', text="Thursday", anchor=W)
        self.tree.heading('day6', text="Friday", anchor=W)
        self.tree.heading('day7', text="Saturday", anchor=W)

        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=25)
        self.tree.column('#2', stretch=NO, minwidth=0, width=90)
        self.tree.column('#3', stretch=NO, minwidth=0, width=90)
        self.tree.column('#4', stretch=YES, minwidth=0, width=150)
        self.tree.column('#5', stretch=NO, minwidth=0, width=90)
        self.tree.column('#6', stretch=NO, minwidth=0, width=90)
        self.tree.column('#7', stretch=YES, minwidth=0, width=250)
        self.tree.column('#8', stretch=NO, minwidth=0, width=90)
        self.tree.column('#9', stretch=NO, minwidth=0, width=0)
        self.tree.column('#10', stretch=NO, minwidth=0, width=0)
        self.tree.column('#11', stretch=NO, minwidth=0, width=0)
        self.tree.column('#12', stretch=NO, minwidth=0, width=0)
        self.tree.column('#13', stretch=NO, minwidth=0, width=0)
        self.tree.column('#14', stretch=NO, minwidth=0, width=0)
        self.tree.column('#15', stretch=NO, minwidth=0, width=0)
        self.tree.column('#16', stretch=NO, minwidth=0, width=0)
        self.tree.column('#17', stretch=NO, minwidth=0, width=0)
        self.tree.column('#18', stretch=NO, minwidth=0, width=0)
        self.tree.column('#19', stretch=NO, minwidth=0, width=0)
        self.tree.pack()
        self.tree.bind('<Double-Button-1>')

        # -------------- Create output status ----------------
        self.txt_output = Label(self.Right_bottom, width=50, font=LARGE_FONT, text="Logged as Instructor", fg="light green")
        self.txt_output.pack(side=TOP, pady=2)

        # ---------------- Table Title ----------------
        self.label = Label(self.BodyTopTitle, text="Select Student", pady=5, font=MEDIUM_FONT)
        self.label.pack(side=TOP)

        # ---------------- INSTRUCTOR SEARCH ----------------
        self.label = Label(self.BodyBottom, text="LESSON BOOKING", pady=5, font=MEDIUM_FONT)
        self.label.pack(side=TOP)

        self.txt_student = Label(self.BodyBottom, text="Select Student", font=SMALL_FONT).place(x=10, y=35)
        self.student_entry = Entry(self.BodyBottom, textvariable=self.FIRSTNAME, bd=2, font=("Arial", 10))
        self.student_entry.place(x=150, y=35, width=200, height=25)

        self.txt_hrate = Label(self.BodyBottom, text="Select Hourely Rate", font=SMALL_FONT).place(x=10, y=75)
        self.hrate_entry = Entry(self.BodyBottom, textvariable=self.HRATE, bd=2, font=("Arial", 10))
        self.hrate_entry.place(x=150, y=75)

        self.txt_style = Label(self.BodyBottom, text="Dance Style", font=SMALL_FONT).place(x=10, y=115)
        self.style_entry = Entry(self.BodyBottom, textvariable=self.STYLE, bd=2, font=("Arial", 10))
        self.style_entry.place(x=150, y=115, width=150, height=25)

        # ---- run fetch student & instructors -----
        self.Read_instructor()
        self.Read_student()

        self.button_clear = Button(self.BodyBottom, text='Clear', width=10, command=self.Clear, background="#0984e3", foreground="white").place(x=150, y=150)

        self.text_instructor = Label(self.BodyBottom, text="Assign Instructor", font=SMALL_FONT).place(x=10, y=190)
        self.instructor = ttk.Combobox(self.BodyBottom, textvariable=self.INSTRUCTOR, font=("Arial", 10))
        self.instructor.set("Select Instructor")
        self.instructor.place(x=150, y=190)

        self.button_book = Button(self.BodyBottom, text='BOOK LESSON', width=15, command=self.LessonBooking, background="#0984e3", foreground="white").place(x=150, y=230)

        # ---------------- TOP BUTTON SECTION ----------------
        self.StudentManagement_btn = Button(self.Top, text="Student Management", width=20, height=2, font=MEDIUM_FONT, state=DISABLED). \
            grid(row=0, column=1, padx=4, pady=5)
        self.InstructorManagement_btn = Button(self.Top, text="Instructor Management", width=20, height=2, font=MEDIUM_FONT, state=DISABLED). \
            grid(row=0, column=2, padx=4, pady=5)
        self.LessonBooking_btn = Button(self.Top, text="Lesson Booking", width=20, height=2, font=MEDIUM_FONT, command=self.tabselect, background="#0984e3", foreground="white"). \
            grid(row=0, column=3, padx=4, pady=5)
        self.exit_btn = Button(self.Top, text="EXIT", width=12, height=2, font=MEDIUM_FONT, command=self.Exit, background="#0984e3", foreground="white"). \
            grid(row=0, column=4, padx=4, pady=5)

    # ---------------- DATABASE CONNECTION ------------
    try:
        connection = sqlite3.connect("DanceFeet_DB.db")
        cursor = connection.cursor()
    except ConnectionError as e:
        print(e)

    def tabselect(self):
        pass

    # ---------- Clear booking ------------
    def Clear(self):
        self.STD_ID.set('')
        self.FIRSTNAME.set('')
        self.STYLE.set('')
        self.HRATE.set('')
        self.INSTRUCTOR.set('')
        self.Read_instructor()

    # ------ Read Student data from Database --------
    def Read_student(self):
        # --------- Read from DB -------------
        self.tree_std.delete(*self.tree_std.get_children())
        self.cursor.execute("SELECT * FROM `students` ORDER BY `id` ASC")
        fetch = self.cursor.fetchall()
        print(fetch)
        for data in fetch:
            self.tree_std.insert('', 'end', values=(
                data[0], data[1], data[8], data[9], data[11]))
            print(data[11])

    # --------- ONCLICK STUDENT --------
    def OnSelected_STD(self, event):
        self.cursorItem = self.tree_std.focus()
        self.contents = (self.tree_std.item(self.cursorItem))
        self.selecteditem = self.contents['values']
        print(self.selecteditem)

        self.instructor['values'] = ("Select Instructor", "")

        self.STD_ID.set(self.selecteditem[0])
        self.FIRSTNAME.set(self.selecteditem[1])
        self.STYLE.set(self.selecteditem[2])
        self.HRATE.set(self.selecteditem[3])
        self.INSTRUCTOR.set(self.selecteditem[4])
        self.Search_Instructors()

    # ---------------- Search -----------------
    def Search_Instructors(self):
        self.tree.place(x=0, y=0, width=1382, height=738)
        print("---Running Read instructor---")
        print(self.student_entry.get())
        print(self.HRATE.get())
        rate = self.HRATE.get()
        style = self.style_entry.get()

        self.tree.place(x=0, y=0, width=1382, height=738)

        # --------- Read from DB -------------

        if style == '' or style == 'Select Style':
            tkMessageBox.showinfo("Error", "Please Fill All Fields")

        else:
            self.tree.delete(*self.tree.get_children())
            self.cursor.execute(
                f"SELECT * FROM instructors WHERE ( hrate < '{rate}') AND dancing_style LIKE '%{style}%' ")
            data = []
            fetch = self.cursor.fetchall()
            print(fetch)
            for data in fetch:
                self.tree.insert('', 'end', values=(
                    data[0], data[1], data[2], data[3], data[4], data[5], data[6],
                    data[7], data[12], data[13], data[14], data[15], data[16],
                    data[17], data[18]))

            self.cursor.execute(f"SELECT * FROM instructors WHERE ( hrate < '{rate}') AND dancing_style LIKE '%{style}%' ")
            data = []
            for self.row in self.cursor.fetchall():
                data.append(self.row[1])
            self.instructor['values'] = data
            print(data)

    # ------- Book lesson ----------
    def LessonBooking(self):
        fname = self.student_entry.get()
        instructor = self.instructor.get()

        print("--- Booking Lesson---")
        print(fname)
        print(instructor)

        # --------- CONVERT LIST TO STRING ---------

        if fname == '' or instructor == '':
            tkMessageBox.showinfo("Error", "Please Fill All Fields")
        else:
            self.tree.delete(*self.tree.get_children())

            self.cursor.execute(f"UPDATE students SET instructor='{instructor}' WHERE firstname = '{fname}'")
            self.connection.commit()
            self.Search_Instructors()
            self.txt_output.config(text="Successfully Booked Lesson", fg="green")
        self.Clear()

    # ============================ CREATE INSTRUCTOR METHODS =============================

    # -------- INSTRUCTOR READ METHOD --------
    def Read_instructor(self):
        self.tree.place(x=0, y=0, width=1382, height=738)
        # --------- Read from DB -------------
        self.tree.delete(*self.tree.get_children())
        self.cursor.execute("SELECT * FROM `instructors` ORDER BY `id` ASC")
        fetch = self.cursor.fetchall()
        for data in fetch:
            self.tree.insert('', 'end', values=(
                data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],
                data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18]))

    # -------- EXIT BUTTON --------
    def Exit(self):
        result = tkMessageBox.askquestion('DanceFeet System', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.instructor_window.destroy()
            exit()


# # ------- interface fore testing purposes ------
# root = Tk()
# gui_instructor = instructor_frame(root)
# root.mainloop()