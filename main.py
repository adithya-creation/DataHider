from tkinter import *
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image, ImageTk
import os
from stegano import lsb
from cryptography.fernet import Fernet
import base64

root = Tk()
root.title("Data Hider - Hide a Secret Text in Image")
root.geometry("750x550+150+100")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

def generate_key(passcode):
    """Generate an encryption key from the passcode"""
    key = base64.urlsafe_b64encode(passcode.ljust(32).encode()[:32])  # Ensure 32 bytes
    return key

def encrypt_message(message, passcode):
    """Encrypt the message using a passcode"""
    key = generate_key(passcode)
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message.decode()

def decrypt_message(encrypted_message, passcode):
    """Decrypt the message using a passcode"""
    try:
        key = generate_key(passcode)
        cipher = Fernet(key)
        decrypted_message = cipher.decrypt(encrypted_message.encode()).decode()
        return decrypted_message
    except Exception:
        return None  # Decryption failed

def showimage():
    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title='Select Image File',
        filetypes=(("PNG file", "*.png"), ("JPG File", "*.jpg"))
    )
    
    img = Image.open(filename)
    img = img.resize((280, 280))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img

def Hide():
    """Hide the encrypted message inside the image"""
    global secret
    message = text1.get(1.0, END).strip()
    if not message:
        messagebox.showwarning("Warning", "Message cannot be empty!")
        return
    
    passcode = simpledialog.askstring("Passcode", "Enter a passcode for encryption:", show='*')
    if not passcode:
        messagebox.showwarning("Warning", "Passcode is required!")
        return
    
    encrypted_message = encrypt_message(message, passcode)
    secret = lsb.hide(str(filename), encrypted_message)
    messagebox.showinfo("Success", "Data hidden successfully!, Click on Save Image to save the image")

def Show():
    """Retrieve and decrypt the hidden message"""
    try:
        encrypted_message = lsb.reveal(filename)
        if not encrypted_message:
            messagebox.showerror("Error", "No hidden data found!")
            return

        passcode = simpledialog.askstring("Passcode", "Enter the passcode to decrypt:", show='*')
        if not passcode:
            messagebox.showwarning("Warning", "Passcode is required!")
            return

        decrypted_message = decrypt_message(encrypted_message, passcode)
        if decrypted_message is None:
            messagebox.showerror("Error", "Incorrect passcode!")
        else:
            text1.delete(1.0, END)
            text1.insert(END, decrypted_message)
            messagebox.showinfo("Success", "Message revealed successfully!")
    
    except Exception:
        messagebox.showerror("Error", "Error retrieving hidden data!")

def save():
    """Save the image with the hidden message"""
    secret.save("hidden.png")
    messagebox.showinfo("Success", "Image saved as hidden.png")

# UI Styling
frame_color = "#282a36"
bg_color = "#1e1e2e"
button_color = "#6272a4"
text_color = "#f8f8f2"

# Icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

# Header
Label(root, text="DATA HIDER IN IMAGE", bg=bg_color, fg="#50fa7b", font=("Arial", 24, "bold")).place(x=200, y=20)

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
Label(frame3, text="Image Operations", bg=frame_color, fg="#ff79c6", font=("Arial", 10, "bold")).place(x=20, y=5)

# Fourth Frame - Data Actions
frame4 = Frame(root, bd=3, bg=frame_color, width=330, height=100, relief=GROOVE)
frame4.place(x=400, y=400)

Button(frame4, text="Hide Data", width=12, height=2, font=("Arial", 12, "bold"), bg=button_color, fg=text_color,
       command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=12, height=2, font=("Arial", 12, "bold"), bg=button_color, fg=text_color,
       command=Show).place(x=180, y=30)
Label(frame4, text="Data Operations", bg=frame_color, fg="#ff79c6", font=("Arial", 10, "bold")).place(x=20, y=5)

root.mainloop()
