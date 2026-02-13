from tkinter import *
from PIL import Image, ImageTk
from PIL.Image import Resampling


class HotelManagementSystem:
    # constructor
    def __init__(self, root):
        self.root = root
        # tkinter UI display setting for window
        self.root.title("Motel Management System")
        self.root.geometry("1440x900+0+0")

        # first image  ======================================================
        img1 = Image.open("./images/atlblurskylinenightsky.png")
        img1 = img1.resize((1440, 180), Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # label for image, and location in root window
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1440, height=180)

        # logo =============================================================
        img2 = Image.open("./images/hunterLicenseBack.jpg")
        img2 = img2.resize((180, 180), Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # label for image, and location in root window
        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=180, height=180)

        # Title  ===========================================================
        lbl_title = Label(
            self.root,
            text="HOTEL MANAGEMENT SYSTEM",
            font=("times new roman", 40, "bold"),
            bg="black",
            fg="silver",
            bd=4,
            relief=RIDGE,
        )
        lbl_title.place(x=0, y=180, width=1440, height=50)

        # main frame  =======================================================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=180, width=1440, height=680)

        # menu ==============================================================
        # label for menu , and location in root window
        lblmenu = Label(
            main_frame,
            text="MENU",
            font=("times new roman", 20, "bold"),
            bg="black",
            fg="silver",
            bd=4,
            relief=RIDGE,
        )
        lblmenu.place(
            x=0,
            y=1,
            width=214,
        )

        # button frame  =======================================================
        button_frame = Frame(main_frame, bd=4, relief=RIDGE)
        button_frame.place(x=0, y=41, width=214, height=195)

        cust_btn = Button(
            button_frame,
            text="CUSTOMER",
            width=18,
            font=("times new roman", 14, "bold"),
            bg="black",
            fg="silver",
            bd=0,
            cursor="hand1",
        )
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(
            button_frame,
            text="ROOM",
            width=18,
            font=("times new roman", 14, "bold"),
            bg="black",
            fg="silver",
            bd=0,
            cursor="hand1",
        )
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(
            button_frame,
            text="DETAILS ",
            width=18,
            font=("times new roman", 14, "bold"),
            bg="black",
            fg="silver",
            bd=0,
            cursor="hand1",
        )
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(
            button_frame,
            text="REPORT",
            width=18,
            font=("times new roman", 14, "bold"),
            bg="black",
            fg="silver",
            bd=0,
            cursor="hand1",
        )
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(
            button_frame,
            text="LOGOUT",
            width=18,
            font=("times new roman", 14, "bold"),
            bg="black",
            fg="silver",
            bd=0,
            cursor="hand1",
        )
        logout_btn.grid(row=4, column=0, pady=1)


# call object for window UI instantiating the object
if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
