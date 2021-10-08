import sqlite3
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as tkMessageBox

# ----- DEFINE CUSTOM FONTS ------
LARGE_FONT = ("Verdana Bold", 18)
MEDIUM_FONT = ("Verdana Bold", 12)
SMALL_FONT = ("Verdana", 8)


class admin_frame(object):
    def __init__(self, window):

        # ---------------- Define Interface ----------------
        self.data = None
        self.row = None
        self.styles_data = []
        self.availability = []
        self.admin_window = window
        self.admin_window.title("DanceFeet - Admin")
        self.admin_window.geometry("1800x900+50+50")
        self.admin_window.resizable(False, False)

        # ---------------- Create Variables for Students ----------------
        self.STD_ID = tkinter.StringVar()
        self.FIRSTNAME = tkinter.StringVar()
        self.SURNAME = tkinter.StringVar()
        self.EMAIL = tkinter.StringVar()
        self.GENDER = tkinter.StringVar()
        self.DOB = tkinter.StringVar()
        self.TP = tkinter.StringVar()
        self.STYLE = tkinter.StringVar()
        self.HRATE = tkinter.StringVar()
        self.INSTRUCTOR = tkinter.StringVar()
        self.INSTRUCTOR_COMBO = tkinter.StringVar()
        self.DAY1 = IntVar()
        self.DAY2 = IntVar()
        self.DAY3 = IntVar()
        self.DAY4 = IntVar()
        self.DAY5 = IntVar()
        self.DAY6 = IntVar()
        self.DAY7 = IntVar()
        self.ADDRESS = tkinter.StringVar()

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
        self.Top = Frame(self.admin_window, bd=4, relief=RIDGE)
        self.Top.pack(side=TOP)

        # -------------- Create Body Frame ----------------
        self.Body = Frame(self.admin_window, bd=3, relief=RIDGE)
        self.Body.place(x=5, y=110, width=400, height=785)

        # -------------- Create Right Frame ----------------
        self.Right = Frame(self.admin_window, bd=3, relief=RIDGE)
        self.Right.place(x=404, y=110, width=1390, height=738)

        # -------------- Create Right Bottom Frame ----------------
        self.Right_bottom = Frame(self.admin_window, bd=3, relief=RIDGE)
        self.Right_bottom.place(x=404, y=845, width=1390, height=50)

        # -------------- Creates tabs for interface ----------------
        self.tab_control = ttk.Notebook(self.Body)

        tab1 = ttk.Frame(self.tab_control)
        tab2 = ttk.Frame(self.tab_control)
        tab3 = ttk.Frame(self.tab_control)

        self.tab_control.add(tab1)
        self.tab_control.add(tab2)
        self.tab_control.add(tab3)
        self.tab_control.pack(expand=1, fill="both")

        # -------------- Student Table view ----------------
        self.tree = ttk.Treeview(self.Right, columns=(
            "id", "fname", "sname", "mail", "address", "gender", "dob", "mobile", "styles", "hrate", "availability", "instructor", "day1", "day2", "day3", "day4", "day5", "day6",
            "day7"),
                                 selectmode="extended",
                                 height=500)

        self.tree.heading('id', text="ID", anchor=W)
        self.tree.heading('fname', text="FirstName", anchor=W)
        self.tree.heading('sname', text="SurName", anchor=W)
        self.tree.heading('mail', text="E-mail", anchor=W)
        self.tree.heading('address', text="Address", anchor=W)
        self.tree.heading('gender', text="Gender", anchor=W)
        self.tree.heading('dob', text="DOB", anchor=W)
        self.tree.heading('mobile', text="Mobile", anchor=W)
        self.tree.heading('styles', text="Styles", anchor=W)
        self.tree.heading('hrate', text="HourlyRate", anchor=W)
        self.tree.heading('availability', text="Availability", anchor=W)
        self.tree.heading('instructor', text="Instructor", anchor=W)
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
        self.tree.column('#4', stretch=YES, minwidth=0, width=170)
        self.tree.column('#5', stretch=NO, minwidth=0, width=140)
        self.tree.column('#6', stretch=NO, minwidth=0, width=70)
        self.tree.column('#7', stretch=NO, minwidth=0, width=90)
        self.tree.column('#8', stretch=NO, minwidth=0, width=90)
        self.tree.column('#9', stretch=NO, minwidth=0, width=120)
        self.tree.column('#10', stretch=NO, minwidth=0, width=70)
        self.tree.column('#11', stretch=NO, minwidth=0, width=300)
        self.tree.column('#12', stretch=YES, minwidth=100)
        self.tree.column('#13', stretch=NO, minwidth=0, width=0)
        self.tree.column('#14', stretch=NO, minwidth=0, width=0)
        self.tree.column('#15', stretch=NO, minwidth=0, width=0)
        self.tree.column('#16', stretch=NO, minwidth=0, width=0)
        self.tree.column('#17', stretch=NO, minwidth=0, width=0)
        self.tree.column('#18', stretch=NO, minwidth=0, width=0)
        self.tree.column('#19', stretch=NO, minwidth=0, width=0)
        self.tree.pack()
        self.tree.bind('<ButtonRelease-1>', self.OnSelected_STD)

        # -------------- Instructor Table view ----------------
        self.tree2 = ttk.Treeview(self.Right, columns=(
            "id", "name", "gender", "style", "mobile", "hrate", "availability", "password", "styles1", "styles2",
            "styles3", "styles4", "day1", "day2", "day3", "day4", "day5", "day6", "day7"), selectmode="extended",
                                  height=500)

        self.tree2.heading('id', text="ID", anchor=W)
        self.tree2.heading('name', text="Name", anchor=W)
        self.tree2.heading('gender', text="Gender", anchor=W)
        self.tree2.heading('style', text="Dancing Style", anchor=W)
        self.tree2.heading('mobile', text="Mobile", anchor=W)
        self.tree2.heading('hrate', text="HourlyRate", anchor=W)
        self.tree2.heading('availability', text="Availability", anchor=W)
        self.tree2.heading('password', text="Password", anchor=W)
        self.tree2.heading('styles1', text="Waltz", anchor=W)
        self.tree2.heading('styles2', text="Jive", anchor=W)
        self.tree2.heading('styles3', text="ChaCha", anchor=W)
        self.tree2.heading('styles4', text="Samba", anchor=W)
        self.tree2.heading('day1', text="Sunday", anchor=W)
        self.tree2.heading('day2', text="Monday", anchor=W)
        self.tree2.heading('day3', text="Tuesday", anchor=W)
        self.tree2.heading('day4', text="Wednesday", anchor=W)
        self.tree2.heading('day5', text="Thursday", anchor=W)
        self.tree2.heading('day6', text="Friday", anchor=W)
        self.tree2.heading('day7', text="Saturday", anchor=W)

        self.tree2.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree2.column('#1', stretch=NO, minwidth=0, width=25)
        self.tree2.column('#2', stretch=NO, minwidth=0, width=90)
        self.tree2.column('#3', stretch=NO, minwidth=0, width=90)
        self.tree2.column('#4', stretch=YES, minwidth=0, width=150)
        self.tree2.column('#5', stretch=NO, minwidth=0, width=90)
        self.tree2.column('#6', stretch=NO, minwidth=0, width=90)
        self.tree2.column('#7', stretch=YES, minwidth=0, width=250)
        self.tree2.column('#8', stretch=NO, minwidth=0, width=90)
        self.tree2.column('#9', stretch=NO, minwidth=0, width=0)
        self.tree2.column('#10', stretch=NO, minwidth=0, width=0)
        self.tree2.column('#11', stretch=NO, minwidth=0, width=0)
        self.tree2.column('#12', stretch=NO, minwidth=0, width=0)
        self.tree2.column('#13', stretch=NO, minwidth=0, width=0)
        self.tree2.column('#14', stretch=NO, minwidth=0, width=0)
        self.tree2.column('#15', stretch=NO, minwidth=0, width=0)
        self.tree2.column('#16', stretch=NO, minwidth=0, width=0)
        self.tree2.column('#17', stretch=NO, minwidth=0, width=0)
        self.tree2.column('#18', stretch=NO, minwidth=0, width=0)
        self.tree2.column('#19', stretch=NO, minwidth=0, width=0)
        self.tree2.pack()
        self.tree2.bind('<ButtonRelease-1>', self.OnSelected_INS)

        # ---------------- TAB SELECT METHOD ---------------
        def tabselect1():
            self.tab_control.select(tab1)
            self.Read_student()
            self.txt_output.config(text="Logged as Admin", fg="light green")
            print("tab01")

        def tabselect2():
            self.tab_control.select(tab2)
            self.Read_instructor()
            self.txt_output.config(text="Logged as Admin", fg="light green")
            print("tab02")

        def tabselect3():
            self.tab_control.select(tab3)
            self.Read_student()
            self.txt_output.config(text="Logged as Admin", fg="light green")
            print("tab03")

        # -------------- Create output status ----------------
        self.txt_output = Label(self.Right_bottom, width=50, font=LARGE_FONT, text="Logged as Admin", fg="light green")
        self.txt_output.pack(side=TOP, pady=2)

        # ---------------- STUDENT TAB ----------------
        self.label = Label(tab1, text="REGISTER STUDENT", pady=5, font=MEDIUM_FONT)
        self.label.pack(side=TOP)

        self.txt_firstname = Label(tab1, text="First Name", font=SMALL_FONT).place(x=10, y=35)
        self.firstname_entry = Entry(tab1, textvariable=self.FIRSTNAME, bd=2, font=("Arial", 10))
        self.firstname_entry.place(x=150, y=35, width=200, height=25)

        self.txt_surname = Label(tab1, text="Surname", font=SMALL_FONT).place(x=10, y=75)
        self.surname_entry = Entry(tab1, textvariable=self.SURNAME, bd=2, font=("Arial", 10))
        self.surname_entry.place(x=150, y=75, width=200, height=25)

        self.txt_email = Label(tab1, text="Email", font=SMALL_FONT).place(x=10, y=115)
        self.email_entry = Entry(tab1, textvariable=self.EMAIL, bd=2, font=("Arial", 10))
        self.email_entry.place(x=150, y=115, width=200, height=25)

        self.txt_address = Label(tab1, text="Address", font=SMALL_FONT).place(x=10, y=155)
        self.address_text = Entry(tab1, textvariable=self.ADDRESS, bd=2, font=("Arial", 10))
        self.address_text.place(x=150, y=155, width=200, height=60)

        self.txt_gender = Label(tab1, text="Gender", font=SMALL_FONT).place(x=10, y=235)
        self.gender_entry = ttk.Combobox(tab1, textvariable=self.GENDER, font=("Arial", 10))
        self.GENDER.set("Select Gender")
        self.gender_entry['values'] = ("Male", "Female")
        self.gender_entry.place(x=150, y=235, width=150, height=25)

        self.txt_dob = Label(tab1, text="Date Of Birth", font=SMALL_FONT).place(x=10, y=275)
        self.dob_entry = Entry(tab1, textvariable=self.DOB, bd=2, font=("Arial", 10))
        self.dob_entry.place(x=150, y=275, width=200, height=25)

        self.txt_tp = Label(tab1, text="Telephone Number", font=SMALL_FONT).place(x=10, y=315)
        self.tp_entry = Entry(tab1, textvariable=self.TP, bd=2, font=("Arial", 10))
        self.tp_entry.place(x=150, y=315, width=200, height=25)

        self.txt_style = Label(tab1, text="Dance Style", font=SMALL_FONT).place(x=10, y=355)
        self.style_menu = ttk.Combobox(tab1, textvariable=self.STYLE, font=("Arial", 10))
        self.STYLE.set("Select Style")
        self.style_menu['value'] = ("Waltz", "Jive", "ChaCha", "Samba")
        self.style_menu.place(x=150, y=355, width=150, height=25)

        self.txt_hourely_rat = Label(tab1, text="Hourly Rate", font=SMALL_FONT).place(x=10, y=455)
        self.hourely_rate_entry = Entry(tab1, textvariable=self.HRATE, bd=2, font=("Arial", 10))
        self.hourely_rate_entry.place(x=150, y=455, width=200, height=25)

        self.txt_instructor = Label(tab1, text="Instructor", font=SMALL_FONT).place(x=10, y=495)
        self.instructor_combo = ttk.Combobox(tab1, font=("Arial", 10), state=DISABLED)
        self.instructor_combo['values'] = ("Move to Lesson Booking", "")
        self.instructor_combo.current(0)
        self.instructor_combo.place(x=150, y=495, width=200, height=25)

        self.txt_availability = Label(tab1, text="Availability", font=SMALL_FONT).place(x=10, y=535)
        self.day1 = Checkbutton(tab1, text="Sunday", variable=self.DAY1, font=("Verdana bold", 8))
        self.day1.place(x=150, y=535)
        self.day2 = Checkbutton(tab1, text="Monday", variable=self.DAY2, font=("Verdana bold", 8))
        self.day2.place(x=150, y=555)
        self.day3 = Checkbutton(tab1, text="Tuesday", variable=self.DAY3, font=("Verdana bold", 8))
        self.day3.place(x=150, y=575)
        self.day4 = Checkbutton(tab1, text="Wednesday", variable=self.DAY4, font=("Verdana bold", 8))
        self.day4.place(x=150, y=595)
        self.day5 = Checkbutton(tab1, text="Thursday", variable=self.DAY5, font=("Verdana bold", 8))
        self.day5.place(x=150, y=615)
        self.day6 = Checkbutton(tab1, text="Friday", variable=self.DAY6, font=("Verdana bold", 8))
        self.day6.place(x=150, y=635)
        self.day7 = Checkbutton(tab1, text="Saturday", variable=self.DAY7, font=("Verdana bold", 8))
        self.day7.place(x=150, y=655)

        self.button_register = Button(tab1, text='ADD', width=10, command=self.submit_student, background="#0984e3",foreground="white").place(
            x=25, y=690)
        self.button_update = Button(tab1, text='UPDATE', width=10, command=self.Update_student, background="#0984e3",
                                    foreground="white").place(x=110, y=690)
        self.button_read = Button(tab1, text='VIEW', width=10, command=self.Read_student, background="#0984e3",
                                  foreground="white").place(x=195, y=690)
        self.button_delete = Button(tab1, text='DELETE', width=10, command=self.Delete_student, background="#0984e3",foreground="white").place(
            x=280, y=690)
        self.button_clear = Button(tab1, text='CLEAR', width=20, command=self.Clear_STD, background="#0984e3",
                                   foreground="white").place(
            x=117, y=725)

        # ---------------- INSTRUCTOR TAB ----------------
        self.label = Label(tab2, text="REGISTER INSTRUCTOR", pady=5, font=MEDIUM_FONT)
        self.label.pack(side=TOP, fill=X)

        self.txt_firstname_instructor = Label(tab2, text="First Name", font=SMALL_FONT).place(x=10, y=35)
        self.firstname_entry_instructor = Entry(tab2, textvariable=self.NAME_INS, bd=2, font=("Arial", 10))
        self.firstname_entry_instructor.place(x=150, y=35, width=200, height=25)

        self.gender_entry = ttk.Combobox(tab2, textvariable=self.GENDER_INS, font=("Arial", 10))
        self.GENDER_INS.set("Select Gender")
        self.gender_entry['values'] = ("Male", "Female")
        self.gender_entry.place(x=150, y=75, width=200, height=25)

        self.txt_styles_instructor = Label(tab2, text="Dancing Style", font=SMALL_FONT).place(x=10, y=115)
        self.txt_style = Label(tab1, text="Dance Style", font=SMALL_FONT).place(x=10, y=355)
        self.style01_instructor = Checkbutton(tab2, text="Waltz", variable=self.STYLE1_INS, font=("Verdana bold", 8))
        self.style01_instructor.place(x=150, y=115)
        self.style02_instructor = Checkbutton(tab2, text="Jive", variable=self.STYLE2_INS, font=("Verdana bold", 8))
        self.style02_instructor.place(x=150, y=135)
        self.style03_instructor = Checkbutton(tab2, text="ChaCha", variable=self.STYLE3_INS, font=("Verdana bold", 8))
        self.style03_instructor.place(x=150, y=155)
        self.style04_instructor = Checkbutton(tab2, text="Samba", variable=self.STYLE4_INS, font=("Verdana bold", 8))
        self.style04_instructor.place(x=150, y=175)

        self.txt_tp_instructor = Label(tab2, text="Telephone Number", font=SMALL_FONT).place(x=10, y=215)
        self.tp_entry_instructor = Entry(tab2, textvariable=self.TP_INS, bd=2, font=("Arial", 10))
        self.tp_entry_instructor.place(x=150, y=215, width=200, height=25)

        self.txt_hourely_rat_instructor = Label(tab2, text="Hourly Rate", font=SMALL_FONT).place(x=10, y=255)
        self.hourely_rate_entry_instructor = Entry(tab2, textvariable=self.HRATE_INS, bd=2, font=("Arial", 10))
        self.hourely_rate_entry_instructor.place(x=150, y=255, width=200, height=25)

        self.txt_availability = Label(tab2, text="Availability", font=SMALL_FONT).place(x=10, y=295)
        self.day1_instructor = Checkbutton(tab2, text="Sunday", variable=self.DAY1_INS, font=("Verdana bold", 8))
        self.day1_instructor.place(x=150, y=295)
        self.day2_instructor = Checkbutton(tab2, text="Monday", variable=self.DAY2_INS, font=("Verdana bold", 8))
        self.day2_instructor.place(x=150, y=315)
        self.day3_instructor = Checkbutton(tab2, text="Tuesday", variable=self.DAY3_INS, font=("Verdana bold", 8))
        self.day3_instructor.place(x=150, y=335)
        self.day4_instructor = Checkbutton(tab2, text="Wednesday", variable=self.DAY4_INS, font=("Verdana bold", 8))
        self.day4_instructor.place(x=150, y=355)
        self.day5_instructor = Checkbutton(tab2, text="Thursday", variable=self.DAY5_INS, font=("Verdana bold", 8))
        self.day5_instructor.place(x=150, y=375)
        self.day6_instructor = Checkbutton(tab2, text="Friday", variable=self.DAY6_INS, font=("Verdana bold", 8))
        self.day6_instructor.place(x=150, y=395)
        self.day7_instructor = Checkbutton(tab2, text="Saturday", variable=self.DAY7_INS, font=("Verdana bold", 8))
        self.day7_instructor.place(x=150, y=415)

        self.txt_password_instructor = Label(tab2, text="Password", font=SMALL_FONT).place(x=10, y=455)
        self.password_entry_instructor = Entry(tab2, textvariable=self.PASSWORD_INS, bd=2, font=("Arial", 10))
        self.password_entry_instructor.place(x=150, y=455, width=200, height=25)

        self.button_register = Button(tab2, text='ADD', width=10, command=self.submit_instructor, background="#0984e3",
                                      foreground="white").place(x=25, y=520)
        self.button_update = Button(tab2, text='UPDATE', width=10, command=self.Update_instructor, background="#0984e3",
                                    foreground="white").place(x=110, y=520)
        self.button_read = Button(tab2, text='VIEW', width=10, command=self.Read_instructor, background="#0984e3",
                                  foreground="white").place(x=195, y=520)
        self.button_delete = Button(tab2, text='DELETE', width=10, command=self.Delete_instructor, background="#0984e3",
                                    foreground="white").place(x=280, y=520)
        self.button_clear = Button(tab2, text='CLEAR', width=20, command=self.Clear_INS, background="#0984e3",
                                   foreground="white").place(
            x=117, y=555)

        # ---------------- LESSON BOOKING TAB ----------------

        self.label = Label(tab3, text="LESSON BOOKING", pady=5, font=MEDIUM_FONT)
        self.label.pack(side=TOP)

        self.txt_firstname = Label(tab3, text="First Name", font=SMALL_FONT).place(x=10, y=35)
        self.firstname_entry = Entry(tab3, textvariable=self.FIRSTNAME, bd=2, font=("Arial", 10), state=DISABLED)
        self.firstname_entry.place(x=150, y=35, width=200, height=25)

        self.txt_surname = Label(tab3, text="Surname", font=SMALL_FONT).place(x=10, y=75)
        self.surname_entry = Entry(tab3, textvariable=self.SURNAME, bd=2, font=("Arial", 10), state=DISABLED)
        self.surname_entry.place(x=150, y=75, width=200, height=25)

        self.txt_email = Label(tab3, text="Email", font=SMALL_FONT).place(x=10, y=115)
        self.email_entry = Entry(tab3, textvariable=self.EMAIL, bd=2, font=("Arial", 10), state=DISABLED)
        self.email_entry.place(x=150, y=115, width=200, height=25)

        self.txt_address = Label(tab3, text="Address", font=SMALL_FONT).place(x=10, y=155)
        self.address_text = Entry(tab3, textvariable=self.ADDRESS, bd=2, font=("Arial", 10), state=DISABLED)
        self.address_text.place(x=150, y=155, width=200, height=60)

        self.txt_gender = Label(tab3, text="Gender", font=SMALL_FONT).place(x=10, y=235)
        self.gender_entry = Entry(tab3, textvariable=self.GENDER, bd=2, font=("Arial", 10), state=DISABLED)
        self.gender_entry.place(x=150, y=235, width=200, height=25)

        self.txt_dob = Label(tab3, text="Date Of Birth", font=SMALL_FONT).place(x=10, y=275)
        self.dob_entry = Entry(tab3, textvariable=self.DOB, bd=2, font=("Arial", 10), state=DISABLED)
        self.dob_entry.place(x=150, y=275, width=200, height=25)

        self.txt_tp = Label(tab3, text="Telephone Number", font=SMALL_FONT).place(x=10, y=315)
        self.tp_entry = Entry(tab3, textvariable=self.TP, bd=2, font=("Arial", 10), state=DISABLED)
        self.tp_entry.place(x=150, y=315, width=200, height=25)

        self.txt_style = Label(tab1, text="Dance Style", font=SMALL_FONT).place(x=10, y=355)
        self.STYLE.set("Select Style")
        self.style01 = ttk.Combobox(tab3, textvariable=self.STYLE, font=("Arial", 10))
        self.style01.place(x=150, y=355, width=150, height=25)

        self.txt_hourely_rat = Label(tab3, text="Hourly Rate", font=SMALL_FONT).place(x=10, y=455)
        self.hourely_rate_entry = Entry(tab3, textvariable=self.HRATE, bd=2, font=("Arial", 10))
        self.hourely_rate_entry.place(x=150, y=455, width=200, height=25)

        self.txt_instructor = Label(tab3, text="Instructor", font=SMALL_FONT).place(x=10, y=495)
        self.instructor_combo = ttk.Combobox(tab3, textvariable=self.INSTRUCTOR, font=("Arial", 10))
        self.INSTRUCTOR.set("Select Instructor")
        self.instructor_combo.place(x=150, y=495, width=200, height=25)

        self.txt_availability = Label(tab3, text="Availability", font=SMALL_FONT).place(x=10, y=535)
        self.day1 = Checkbutton(tab3, text="Sunday", variable=self.DAY1, font=("Verdana bold", 8))
        self.day1.place(x=150, y=535)
        self.day2 = Checkbutton(tab3, text="Monday", variable=self.DAY2, font=("Verdana bold", 8))
        self.day2.place(x=150, y=555)
        self.day3 = Checkbutton(tab3, text="Tuesday", variable=self.DAY3, font=("Verdana bold", 8))
        self.day3.place(x=150, y=575)
        self.day4 = Checkbutton(tab3, text="Wednesday", variable=self.DAY4, font=("Verdana bold", 8))
        self.day4.place(x=150, y=595)
        self.day5 = Checkbutton(tab3, text="Thursday", variable=self.DAY5, font=("Verdana bold", 8))
        self.day5.place(x=150, y=615)
        self.day6 = Checkbutton(tab3, text="Friday", variable=self.DAY6, font=("Verdana bold", 8))
        self.day6.place(x=150, y=635)
        self.day7 = Checkbutton(tab3, text="Saturday", variable=self.DAY7, font=("Verdana bold", 8))
        self.day7.place(x=150, y=655)

        self.button_register = Button(tab3, text='ADD', width=10, command=self.submit_student, state=DISABLED).place(
            x=25, y=690)
        self.button_update = Button(tab3, text='UPDATE', width=10, command=self.Update_student, background="#0984e3",
                                    foreground="white").place(x=110, y=690)
        self.button_read = Button(tab3, text='VIEW', width=10, command=self.Read_student, background="#0984e3",
                                  foreground="white").place(x=195, y=690)
        self.button_delete = Button(tab3, text='DELETE', width=10, command=self.Delete_student, state=DISABLED).place(
            x=280, y=690)
        self.button_clear = Button(tab3, text='CLEAR', width=20, command=self.Clear_STD, background="#0984e3",
                                   foreground="white").place(
            x=117, y=725)

        # # ---------------- TOP BUTTON SECTION ----------------

        self.StudentManagement_btn = Button(self.Top, text="Student Management", width=20, height=2, font=MEDIUM_FONT,
                                            command=tabselect1, background="#0984e3", foreground="white"). \
            grid(row=0, column=1, padx=4, pady=5)
        self.InstructorManagement_btn = Button(self.Top, text="Instructor Management", width=20, height=2,
                                               font=MEDIUM_FONT, command=tabselect2, background="#0984e3",
                                               foreground="white"). \
            grid(row=0, column=2, padx=4, pady=5)
        self.LessonBooking_btn = Button(self.Top, text="Lesson Booking", width=20, height=2, font=MEDIUM_FONT,
                                        command=tabselect3, background="#0984e3", foreground="white"). \
            grid(row=0, column=3, padx=4, pady=5)
        self.exit_btn = Button(self.Top, text="EXIT", width=12, height=2, font=MEDIUM_FONT, command=self.Exit,
                               background="#0984e3", foreground="white"). \
            grid(row=0, column=4, padx=4, pady=5)

    # ---------------- DATABASE CONNECTION ------------
    try:
        connection = sqlite3.connect("DanceFeet_DB.db")
        cursor = connection.cursor()
    except ConnectionError as e:
        print(e)

    # ============================ CREATE STUDENT METHODS =============================

    # ---------------- Create Clear Functions --------------
    def Clear_STD(self):

        self.FIRSTNAME.set('')
        self.SURNAME.set('')
        self.EMAIL.set('')
        self.ADDRESS.set('')
        self.GENDER.set('')
        self.DOB.set('')
        self.TP.set('')
        self.instructor_combo.set('Select Instructor')
        self.instructor_combo['values'] = ("Select Instructor", "")
        self.STYLE.set('Select Style')
        self.HRATE.set('')
        self.DAY1.set('0')
        self.DAY2.set('0')
        self.DAY3.set('0')
        self.DAY4.set('0')
        self.DAY5.set('0')
        self.DAY6.set('0')
        self.DAY7.set('0')
        self.availability = []
        self.styles_data = []

    # ---------------- Student Register button method ---------------
    def submit_student(self):
        fname = self.FIRSTNAME.get()
        sname = self.SURNAME.get()
        email = self.EMAIL.get()
        address = self.ADDRESS.get()
        gender = self.GENDER.get()
        dob = self.DOB.get()
        tp = self.TP.get()
        style = self.STYLE.get()
        hourely = self.HRATE.get()
        day1 = self.DAY1.get()
        day2 = self.DAY2.get()
        day3 = self.DAY3.get()
        day4 = self.DAY4.get()
        day5 = self.DAY5.get()
        day6 = self.DAY6.get()
        day7 = self.DAY7.get()

        # ------ SET WEEK DAY LIST USING CHECKBOX -------
        if day1 == 1:
            self.availability.append('Sunday')
        if day2 == 1:
            self.availability.append('Monday')
        if day3 == 1:
            self.availability.append('Tuesday')
        if day4 == 1:
            self.availability.append('Wednesday')
        if day5 == 1:
            self.availability.append('Thursday')
        if day6 == 1:
            self.availability.append('Friday')
        if day7 == 1:
            self.availability.append('Saturday')

        print("--- submit student---")
        print(self.styles_data)
        print(self.availability)

        # --------- CONVERT LIST TO STRING ---------
        style_str = ','.join(self.styles_data)
        availability_str = ','.join(self.availability)
        print(style_str)
        print(availability_str)

        if fname == '' or sname == '' or email == '' or address == '' or gender == 'Select Gender' or dob == '' or style == 'Select Style' or tp == '' or availability_str == '':
            tkMessageBox.showinfo("Error", "Please Fill All Fields")

        else:
            insert_statement = f"INSERT INTO students(firstname,surname,email,address,gender,dob,mobile," \
                               f"styles_data,hrate,availability,Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday) " \
                               f"VALUES ('{fname}','{sname}','{email}','{address}','{gender}','{dob}','{tp}','{style}','{hourely}','{availability_str}','{day1}','{day2}','{day3}','{day4}','{day5}','{day6}','{day7}') "

            self.cursor.execute(insert_statement)
            self.connection.commit()
            self.Clear_STD()
            self.Read_student()
            self.txt_output.config(text="Student Record Added Successfully", fg="purple")

    # ---------------- Create Methods ----------------
    def OnSelected_STD(self, event):
        self.cursorItem = self.tree.focus()
        self.contents = (self.tree.item(self.cursorItem))
        self.selecteditem = self.contents['values']
        print(self.selecteditem)

        self.Clear_STD()
        self.instructor_combo['values'] = ("Select Instructor", "")

        self.STD_ID.set(self.selecteditem[0])
        self.FIRSTNAME.set(self.selecteditem[1])
        self.SURNAME.set(self.selecteditem[2])
        self.EMAIL.set(self.selecteditem[3])
        self.ADDRESS.set(self.selecteditem[4])
        self.GENDER.set(self.selecteditem[5])
        self.DOB.set(self.selecteditem[6])
        self.TP.set(self.selecteditem[7])
        self.STYLE.set(self.selecteditem[8])
        self.HRATE.set(self.selecteditem[9])
        self.INSTRUCTOR.set(self.selecteditem[11])
        self.DAY1.set(self.selecteditem[12])
        self.DAY2.set(self.selecteditem[13])
        self.DAY3.set(self.selecteditem[14])
        self.DAY4.set(self.selecteditem[15])
        self.DAY5.set(self.selecteditem[16])
        self.DAY6.set(self.selecteditem[17])
        self.DAY7.set(self.selecteditem[18])
        self.instructor_combo['values'] = self.combo_values_input(self.selecteditem[9], self.selecteditem[8],
                                                                  self.selecteditem[10])

    # --------- GET COMBO BOX VALUES FROM DATABASE ----------
    def combo_values_input(self, student_rate, student_style, student_availability):
        print("--- Selecting Instructor ---")
        temp = self.STYLE.get()
        print(temp)
        self.cursor.execute(f"SELECT name FROM instructors WHERE hrate <= {student_rate} AND (Sunday = {self.DAY1.get()} "
                            f"OR Monday = {self.DAY2.get()} OR Tuesday = {self.DAY3.get()} "
                            f"OR Wednesday = {self.DAY4.get()} OR Thursday = {self.DAY5.get()} OR Friday = {self.DAY6.get()} "
                            f"OR Saturday = {self.DAY7.get()}) AND (dancing_style  LIKE '%{temp}%') ")
        data = []
        for self.row in self.cursor.fetchall():
            data.append(self.row[0])
            print(self.row[0])
        print(data)
        return data

    # -------- UPDATE STUDENT METHOD --------
    def Update_student(self):
        std_id = self.STD_ID.get()
        fname = self.FIRSTNAME.get()
        sname = self.SURNAME.get()
        email = self.EMAIL.get()
        address = self.ADDRESS.get()
        gender = self.GENDER.get()
        dob = self.DOB.get()
        tp = self.TP.get()
        style = self.STYLE.get()
        hourely = self.HRATE.get()
        instructor = self.instructor_combo.get()
        print("instructor", instructor)
        day1 = self.DAY1.get()
        day2 = self.DAY2.get()
        day3 = self.DAY3.get()
        day4 = self.DAY4.get()
        day5 = self.DAY5.get()
        day6 = self.DAY6.get()
        day7 = self.DAY7.get()

        # ------ SET WEEK DAY LIST USING CHECKBOX -------
        if day1 == 1:
            self.availability.append('Sunday')
        if day2 == 1:
            self.availability.append('Monday')
        if day3 == 1:
            self.availability.append('Tuesday')
        if day4 == 1:
            self.availability.append('Wednesday')
        if day5 == 1:
            self.availability.append('Thursday')
        if day6 == 1:
            self.availability.append('Friday')
        if day7 == 1:
            self.availability.append('Saturday')

        print("--- update student---")
        print(self.availability)

        # --------- CONVERT LIST TO STRING ---------
        style_str = ','.join(self.styles_data)
        availability_str = ','.join(self.availability)
        print(style_str)
        print(availability_str)

        if fname == '' or sname == '' or email == '' or address == '' or gender == '' or dob == '' or availability_str == '' or style == '' or tp == '' or hourely == '':
            tkMessageBox.showinfo("Error", "Please Fill All Fields")
        else:
            self.tree.delete(*self.tree.get_children())

            self.cursor.execute(
                f"UPDATE `students` SET `firstname` = '{fname}', `surname` = '{sname}', `email` = '{email}','address' = '{address}',"
                f"`gender` = '{gender}',  `dob` = '{dob}', `mobile` = '{tp}',"
                f"'hrate' = '{hourely}','availability'='{availability_str}',"
                f"'instructor'='{instructor}','Sunday'='{day1}','Monday'='{day2}','Tuesday'='{day3}','Wednesday'='{day4}','Thursday'='{day5}','Friday'='{day6}',"
                f"'Saturday'='{day7}','styles_data'='{style}' WHERE `id` = '{std_id}'")
            self.connection.commit()
            self.cursor.execute("SELECT * FROM `students` ORDER BY `firstname` ASC")
            fetch = self.cursor.fetchall()
            for self.data in fetch:
                self.tree.insert('', 'end', values=(
                    self.data[0], self.data[1], self.data[2], self.data[3], self.data[4], self.data[5], self.data[6],
                    self.data[7], self.data[12], self.data[13], self.data[14], self.data[15], self.data[16],
                    self.data[17], self.data[18]))
            self.Read_student()
            self.Clear_STD()
            self.txt_output.config(text="Student Record Successfully Updated", fg="green")

    # -------- READ STUDENT METHOD --------
    def Read_student(self):
        self.tree.place(x=0, y=0, width=1382, height=738)
        self.tree2.place(x=10000, y=10000, width=995, height=585)
        # --------- Read from DB -------------
        self.tree.delete(*self.tree.get_children())
        self.cursor.execute("SELECT * FROM `students` ORDER BY `id` ASC")
        fetch = self.cursor.fetchall()
        for data in fetch:
            self.tree.insert('', 'end', values=(
                data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],
                data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18]))

    # -------- DELETE STUDENT METHOD --------
    def Delete_student(self):
        if not self.tree.selection():
            # self.txt_result.config(text="Please select an item first", fg="red")
            pass
        else:
            result = tkMessageBox.askquestion('Instructor Management - DanceFeet System',
                                              'Are you sure you want to delete this record?', icon="warning")
            if result == 'yes':
                self.cursorItem = self.tree.focus()
                self.contents = (self.tree.item(self.cursorItem))
                self.selecteditem = self.contents['values']
                self.tree.delete(self.cursorItem)
                self.cursor.execute(f"DELETE FROM `students` WHERE `id` = '{self.selecteditem[0]}'")
                self.connection.commit()
                self.txt_output.config(text="Student Record Deleted", fg="red")

    # ============================ CREATE INSTRUCTOR METHODS =============================

    # -------- INSTRUCTOR CLEAR METHOD --------
    def Clear_INS(self):
        self.NAME_INS.set('')
        self.GENDER_INS.set('')
        self.STYLE_INS.set('')
        self.TP_INS.set('')
        self.HRATE_INS.set('')
        self.AVAILABILITY_INS.set('')
        self.PASSWORD_INS.set('')
        self.STYLE1_INS.set('0')
        self.STYLE2_INS.set('0')
        self.STYLE3_INS.set('0')
        self.STYLE4_INS.set('0')
        self.DAY1_INS.set('0')
        self.DAY2_INS.set('0')
        self.DAY3_INS.set('0')
        self.DAY4_INS.set('0')
        self.DAY5_INS.set('0')
        self.DAY6_INS.set('0')
        self.DAY7_INS.set('0')
        self.availability = []
        self.styles_data = []

    # ---------------- Student Register button method ---------------
    def submit_instructor(self):

        temp = "instructor"

        ins_name = self.NAME_INS.get()
        ins_gender = self.GENDER_INS.get()
        ins_tp = self.TP_INS.get()
        ins_hourely = self.HRATE_INS.get()
        ins_password = self.PASSWORD_INS.get()
        style1 = self.STYLE1_INS.get()
        style2 = self.STYLE2_INS.get()
        style3 = self.STYLE3_INS.get()
        style4 = self.STYLE4_INS.get()
        day1 = self.DAY1_INS.get()
        day2 = self.DAY2_INS.get()
        day3 = self.DAY3_INS.get()
        day4 = self.DAY4_INS.get()
        day5 = self.DAY5_INS.get()
        day6 = self.DAY6_INS.get()
        day7 = self.DAY7_INS.get()

        # ------ SET STYLE LIST USING CHECKBOX -------
        if style1 == 1:
            self.styles_data.append('Waltz')
        if style2 == 1:
            self.styles_data.append('Jive')
        if style3 == 1:
            self.styles_data.append('ChaCha')
        if style4 == 1:
            self.styles_data.append('Samba')

        # ------ SET WEEK DAY LIST USING CHECKBOX -------
        if day1 == 1:
            self.availability.append('Sunday')
        if day2 == 1:
            self.availability.append('Monday')
        if day3 == 1:
            self.availability.append('Tuesday')
        if day4 == 1:
            self.availability.append('Wednesday')
        if day5 == 1:
            self.availability.append('Thursday')
        if day6 == 1:
            self.availability.append('Friday')
        if day7 == 1:
            self.availability.append('Saturday')

        print("--- submit instructor---")
        print(self.styles_data)
        print(self.availability)

        # --------- CONVERT LIST TO STRING ---------
        style_str = ', '.join(self.styles_data)
        availability_str = ','.join(self.availability)
        print(style_str)
        print(availability_str)
        print(ins_gender)

        if ins_name == '' or ins_gender == '' or style_str == '' or ins_tp == '' or availability_str == '' or ins_hourely == '' or ins_password == '':
            tkMessageBox.showinfo("Error", "Please Fill All Fields")

        else:
            insert_statement = f"INSERT INTO instructors(name,gender,dancing_style,mobile,hrate,availability,password,Waltz,Jive,ChaCha,Samba,Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday) " \
                               f"VALUES ('{ins_name}','{ins_gender}','{style_str}','{ins_tp}','{ins_hourely}','{availability_str}','{ins_password}','{style1}','{style2}','{style3}','{style4}','{day1}','{day2}','{day3}','{day4}','{day5}','{day6}','{day7}') "
            insert_user = f"INSERT INTO users(username,password,privilege) VALUES ('{ins_name}','{ins_password}','{temp}')"
            self.cursor.execute(insert_statement)
            self.cursor.execute(insert_user)
            self.connection.commit()
            self.Read_instructor()
            self.Clear_INS()
            self.txt_output.config(text="Instructor Record Added Successfully", fg="purple")

    # -------- INSTRUCTOR ONSELECT METHOD --------
    def OnSelected_INS(self, event):
        self.cursorItem = self.tree2.focus()
        self.contents = (self.tree2.item(self.cursorItem))
        self.selecteditem = self.contents['values']
        print("--- ON SELECTED ---")
        print(self.selecteditem)

        self.Clear_INS()

        self.INS_ID.set(self.selecteditem[0])
        self.NAME_INS.set(self.selecteditem[1])
        self.GENDER_INS.set(self.selecteditem[2])
        self.TP_INS.set(self.selecteditem[4])
        self.HRATE_INS.set(self.selecteditem[5])
        self.PASSWORD_INS.set(self.selecteditem[7])
        self.STYLE1_INS.set(self.selecteditem[8])
        self.STYLE2_INS.set(self.selecteditem[9])
        self.STYLE3_INS.set(self.selecteditem[10])
        self.STYLE4_INS.set(self.selecteditem[11])
        self.DAY1_INS.set(self.selecteditem[12])
        self.DAY2_INS.set(self.selecteditem[13])
        self.DAY3_INS.set(self.selecteditem[14])
        self.DAY4_INS.set(self.selecteditem[15])
        self.DAY5_INS.set(self.selecteditem[16])
        self.DAY6_INS.set(self.selecteditem[17])
        self.DAY7_INS.set(self.selecteditem[18])

    # -------- INSTRUCTOR UPDATE METHOD --------

    def Update_instructor(self):

        print("Running Updater...")

        ins_id = self.INS_ID.get()
        ins_name = self.NAME_INS.get()
        ins_gender = self.GENDER_INS.get()
        ins_tp = self.TP_INS.get()
        ins_hourely = self.HRATE_INS.get()
        ins_password = self.PASSWORD_INS.get()
        style1 = self.STYLE1_INS.get()
        style2 = self.STYLE2_INS.get()
        style3 = self.STYLE3_INS.get()
        style4 = self.STYLE4_INS.get()
        day1 = self.DAY1_INS.get()
        day2 = self.DAY2_INS.get()
        day3 = self.DAY3_INS.get()
        day4 = self.DAY4_INS.get()
        day5 = self.DAY5_INS.get()
        day6 = self.DAY6_INS.get()
        day7 = self.DAY7_INS.get()

        # ------ SET STYLE LIST USING CHECKBOX -------
        if style1 == 1:
            self.styles_data.append('Waltz')
        if style2 == 1:
            self.styles_data.append('Jive')
        if style3 == 1:
            self.styles_data.append('ChaCha')
        if style4 == 1:
            self.styles_data.append('Samba')

        # ------ SET WEEK DAY LIST USING CHECKBOX -------
        if day1 == 1:
            self.availability.append('Sunday')
        if day2 == 1:
            self.availability.append('Monday')
        if day3 == 1:
            self.availability.append('Tuesday')
        if day4 == 1:
            self.availability.append('Wednesday')
        if day5 == 1:
            self.availability.append('Thursday')
        if day6 == 1:
            self.availability.append('Friday')
        if day7 == 1:
            self.availability.append('Saturday')

        print("--- update instructor---")
        print(self.styles_data)
        print(self.availability)

        # --------- CONVERT LIST TO STRING ---------
        style_str = ','.join(self.styles_data)
        availability_str = ','.join(self.availability)
        print(style_str)
        print(availability_str)
        print(ins_gender)

        if ins_name == '' or ins_gender == '' or style_str == '' or ins_tp == '' or ins_hourely == '' or availability_str == '' or ins_password == '':
            tkMessageBox.showinfo("Error", "Please Fill All Fields")
        else:
            self.tree2.delete(*self.tree2.get_children())
            user_statement = f"UPDATE 'users' SET 'username' = '{ins_name}', 'password' = '{ins_password}' WHERE `username` = '{ins_name}'"
            self.cursor.execute(
                f"UPDATE `instructors` SET `name` = '{ins_name}', `gender` = '{ins_gender}', `dancing_style` = '{style_str}',"
                f"'mobile' = '{ins_tp}', `hrate` = '{ins_hourely}',  `availability` = '{availability_str}',"
                f"`password` = '{ins_password}',`Waltz` = '{style1}',`Jive` = '{style2}',`ChaCha` = '{style3}',`Samba` = '{style4}',"
                f"'Sunday'='{day1}','Monday'='{day2}','Tuesday'='{day3}','Wednesday'='{day4}','Thursday'='{day5}','Friday'='{day6}','Saturday'='{day7}'"
                f" WHERE `id` = '{ins_id}'")
            self.cursor.execute(user_statement)
            self.connection.commit()
            self.cursor.execute("SELECT * FROM `instructors` ORDER BY `id` ASC")
            fetch = self.cursor.fetchall()
            for self.data in fetch:
                self.tree2.insert('', 'end', values=(
                    self.data[0], self.data[1], self.data[2], self.data[3], self.data[4], self.data[5], self.data[6], self.data[7], self.data[8], self.data[9], self.data[10], self.data[11], self.data[12], self.data[13], self.data[14], self.data[15], self.data[16], self.data[17] ))
            self.Clear_INS()
            self.Read_instructor()
            self.txt_output.config(text="Instructor Record Successfully Updated", fg="green")

    # -------- INSTRUCTOR READ METHOD --------
    def Read_instructor(self):
        self.tree.place(x=5000, y=0, width=995, height=585)
        self.tree2.place(x=0, y=0, width=1382, height=738)

        # --------- Read from DB -------------
        self.tree2.delete(*self.tree2.get_children())
        self.cursor.execute("SELECT * FROM `instructors` ORDER BY `id` ASC")
        fetch = self.cursor.fetchall()
        for data in fetch:
            self.tree2.insert('', 'end', values=(
                data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],
                data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18]))

    # -------- INSTRUCTOR DELETE METHOD --------
    def Delete_instructor(self):
        print("--- Delete Instructor ---")
        if not self.tree2.selection():
            # self.txt_result.config(text="Please select an item first", fg="red")
            pass
        else:
            result = tkMessageBox.askquestion('Instructor Management - DanceFeet System',
                                              'Are you sure you want to delete this record?', icon="warning")
            if result == 'yes':
                self.cursorItem = self.tree2.focus()
                self.contents = (self.tree2.item(self.cursorItem))
                self.selecteditem = self.contents['values']
                self.tree2.delete(self.cursorItem)
                self.cursor.execute(f"DELETE FROM `instructors` WHERE `id` = '{self.selecteditem[0]}'")
                print(self.selecteditem[1])
                self.cursor.execute(f"DELETE FROM `users` WHERE `username` = '{self.selecteditem[1]}'")
                self.connection.commit()
                self.txt_output.config(text="Instructor Record Deleted", fg="red")

    # -------- EXIT BUTTON --------
    def Exit(self):
        result = tkMessageBox.askquestion('DanceFeet System', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.admin_window.destroy()
            exit()


# ------- interface fore testing purposes ------
# root = Tk()
# gui_admin = admin_frame(root)
# root.mainloop()