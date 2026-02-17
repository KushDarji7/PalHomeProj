from tkinter import*
from PIL import Image, ImageTk
from PIL.Image import Resampling


class Customer_Win:
    # constructor
    def __init__(self, root):
        self.root = root
        # tkinter UI display setting for window
        self.root.title("Customer Window")
        self.root.geometry("1225x680+214+180")

        # Title  ===========================================================
        lbl_title = Label(
            self.root,
            text="ADD CUSTOMER DETAILS",
            font=("times new roman", 40, "bold"),
            bg="black",
            fg="silver",
            bd=4,
            relief=RIDGE,
        )
        lbl_title.place(x=0, y=0, width=1225, height=50)

        # logo =============================================================
        img2 = Image.open("./images/hunterLicenseBack.jpg")
        img2 = img2.resize((65, 40), Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # label for image, and location in root window
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=4, y=4, width=65, height=40)


if __name__ == "__main__":
    root = Tk()
    obj = Customer_Win(root)
    root.mainloop()
