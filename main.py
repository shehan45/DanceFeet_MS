from login import login_frame
from tkinter import *


class main:

    def RunLogin(self):
        root = Tk()
        gui = login_frame(root)
        root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main.RunLogin()
