from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from stegano import lsb

root = Tk()
root.title("Data Hider - Hide a secret text in image")
root.geometry("750x550+150+100")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

def showimage():
    global filename
    filename = filedialog.askopenfilename(
    initialdir=os.getcwd(),
    title='Select Image File',
    filetype=(("PNG file", "*.png"), ("JPG File", "*.jpg"), ("Text File", "*.txt"))
)

    img = Image.open(filename)
    img = img.resize((280, 280))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img

def Hide():
    global secret
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)

def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

def save():
    secret.save("hidden.png")

# UI Styling
frame_color = "#282a36"
bg_color = "#1e1e2e"
button_color = "#6272a4"
text_color = "#f8f8f2"

# Icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

# Header
Label(root, text="DATA HIDER IN IMAGE", bg=bg_color, fg="#50fa7b", font=("Arial", 24, "bold"))\
    .place(x=200, y=20)

# First Frame - Image Preview
f = Frame(root, bd=3, bg=frame_color, width=300, height=300, relief=GROOVE)
f.place(x=20, y=80)

lbl = Label(f, bg=frame_color)
lbl.place(x=20, y=10)

# Second Frame - Text Input
frame2 = Frame(root, bd=3, width=350, height=300, bg=frame_color, relief=GROOVE)
frame2.place(x=380, y=80)

text1 = Text(frame2, font=("Arial", 12), bg=frame_color, fg=text_color, relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=340, height=290)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=330, y=0, height=300)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Third Frame - Image Actions
frame3 = Frame(root, bd=3, bg=frame_color, width=330, height=100, relief=GROOVE)
frame3.place(x=20, y=400)

Button(frame3, text="Open Image", width=12, height=2, font=("Arial", 12, "bold"), bg=button_color, fg=text_color,
       command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=12, height=2, font=("Arial", 12, "bold"), bg=button_color, fg=text_color,
       command=save).place(x=180, y=30)
Label(frame3, text="Image Operations", bg=frame_color, fg="#ff79c6", font=("Arial", 10, "bold"))\
    .place(x=20, y=5)

# Fourth Frame - Data Actions
frame4 = Frame(root, bd=3, bg=frame_color, width=330, height=100, relief=GROOVE)
frame4.place(x=400, y=400)

Button(frame4, text="Hide Data", width=12, height=2, font=("Arial", 12, "bold"), bg=button_color, fg=text_color,
       command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=12, height=2, font=("Arial", 12, "bold"), bg=button_color, fg=text_color,
       command=Show).place(x=180, y=30)
Label(frame4, text="Data Operations", bg=frame_color, fg="#ff79c6", font=("Arial", 10, "bold"))\
    .place(x=20, y=5)

root.mainloop()

#By Adithya Mittapally