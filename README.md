# Data Hider in Image Using Steganography

## Introduction
This project provides a graphical user interface (GUI) application for hiding and revealing secret text inside images using **LSB (Least Significant Bit) Steganography**. The goal is to securely embed hidden messages within images without altering their visual appearance.

## Features
- **Hide Secret Messages**: Securely embed text inside an image.
- **Retrieve Hidden Data**: Extract the hidden message from an image.
- **Passcode Protection**: Encrypt hidden messages with a user-defined passcode.
- **Simple and Modern GUI**: User-friendly interface with enhanced styling.
- **Supports Multiple Image Formats**: Works with PNG and JPG files.

## Technologies Used
- **Programming Language**: Python
- **GUI Library**: Tkinter
- **Image Processing**: Pillow (PIL)
- **Steganography**: Stegano
- **Encryption**: Cryptography (Fernet)

## Installation
### Prerequisites
Ensure you have Python installed (version 3.6+ recommended).

### Steps to Install Dependencies
```sh
pip install pillow stegano cryptography
```

## How to Use
### 1. Open the Application
Run the script using:
```sh
python main.py
```

### 2. Select an Image
- Click on "Open Image" to choose an image for hiding text.

### 3. Hide Data
- Enter the secret message in the text box.
- Provide a **passcode** for encryption.
- Click on "Hide Data" to embed the encrypted text inside the image.
- Save the steganographic image using "Save Image".

### 4. Retrieve Hidden Data
- Click "Show Data" to extract and display the hidden text.
- Enter the correct passcode to decrypt the message.

## Future Scope
- Support for additional image formats (GIF, BMP, TIFF).
- Implementation of AES/RSA encryption before embedding text.
- Mobile app version for Android/iOS.
- Cloud-based steganography service for remote access.

## License
This project is licensed under the MIT License.

## Author
Developed by **Adithya Mittapally**.

