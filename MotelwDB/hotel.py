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
        lbl_title.place(x=0,y=180,width=1440, height=50)

        # main frame  =======================================================
        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=230, width=1440, height=670)

# call object for window UI instantiating the object
if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
