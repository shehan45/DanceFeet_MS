from tkinter import *
import sqlite3
import tkinter.messagebox as MessageBox
from admin import admin_frame
from instructor import instructor_frame

# ----- DEFINE CUSTOM FONTS ------
LARGE_FONT = ("Verdana Bold", 18)
MEDIUM_FONT = ("Verdana", 12)
MEDIUM_FONT_ERROR = ("Verdana bold", 12)
SMALL_FONT = ("Verdana", 8)

# ----- CREATE WINDOWS FOR INTERFACES ------


def admin_area():
    root.destroy()
    window2 = Tk()
    admin_frame(window2)
    window2.mainloop()


def instructor_area():
    root.destroy()
    window3 = Tk()
    instructor_frame(window3)
    window3.mainloop()

# ----- DEFINE EXIT BUTTON ------


def Exit():
    result = MessageBox.askquestion('DanceFeet', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


class login_frame(object):
    def __init__(self, window):

        self.root = window
        self.root.title("DanceFeet")
        self.root.geometry("597x220+600+350")
        self.root.resizable(False, False)

        self.label = Label(window, text="USER LOGIN", font=LARGE_FONT)
        self.label.pack(side=TOP, fill=X, pady=10)

        self.login_frame = Frame(self.root, bd=0, relief=RIDGE)
        self.login_frame.place(x=0, y=60, width=595, height=150)

        self.usernameLabel = Label(self.login_frame, text="Enter your username", font=MEDIUM_FONT)
        self.usernameLabel.grid(row=1, columnspan=2, pady=10, padx=30)

        self.usernameEntry = Entry(self.login_frame, width=50)
        self.usernameEntry.grid(row=1, column=2)

        self.passwordLabel = Label(self.login_frame, text="Enter your Password", font=MEDIUM_FONT)
        self.passwordLabel.grid(row=2, columnspan=2, pady=10, padx=30)

        self.passwordEntry = Entry(self.login_frame, width=50, show='*')
        self.passwordEntry.grid(row=2, column=2)

        # ----------- Create error label -------------
        self.txt_error = Label(self.login_frame, width=30, font=MEDIUM_FONT, text="")
        self.txt_error.place(x=145, y=90)

        # ----------- Define Button Frame ------------

        self.button_frame = Frame(self.root, pady=5, relief=RIDGE)
        self.button_frame.pack(side=BOTTOM)

        self.greet_button = Button(self.button_frame, width=10, background="#0984e3", foreground="white", height=1, text="LOGIN", command=self.login)
        self.greet_button.grid(row=0, column=1, padx=5, pady=5)

        self.close_button = Button(self.button_frame, width=10, background="#0984e3", foreground="white", height=1, text="EXIT", command=Exit)
        self.close_button.grid(row=0, column=2, padx=5, pady=5)

    # -------- CREATE DATABASE CONNECTION ---------
    try:
        connection = sqlite3.connect("DanceFeet_DB.db")
        cursor = connection.cursor()
    except ConnectionError as e:
        print(e)

    # -------- CREATE METHODS ---------
    def login(self):
        print("Executing Login")
        user = self.usernameEntry.get()
        password = self.passwordEntry.get()
        print(user, password)

        privilege_admin = "admin"
        privilege_instructor = "instructor"

        # ------- Checking for Empty logging --------
        if user == '' or password == '':
            self.txt_error = Label(self.login_frame, width=30, font=MEDIUM_FONT_ERROR, text="Fill All Fields!", fg="black")
            self.txt_error.place(x=130, y=90)
        else:
            while 1:
                # ------- Checking for Empty logging --------
                print("Checking Privilege")
                valid_statement = f"SELECT privilege from users WHERE username='{user}' AND Password = '{password}';"
                self.cursor.execute(valid_statement)
                privilege = self.cursor.fetchall()

                # ------- Check privilege and redirect user --------
                if len(privilege) == 1:
                    if privilege[0][0] == privilege_admin:
                        print("admin")
                        admin_area()

                    elif privilege[0][0] == privilege_instructor:
                        print("instructor")
                        instructor_area()
                    pass

                else:
                    self.txt_error = Label(self.login_frame, width=30, font=MEDIUM_FONT, text="Incorrect Login",
                                           fg="black")
                    self.txt_error.place(x=130, y=90)
                break


root = Tk()
gui = login_frame(root)
root.mainloop()
