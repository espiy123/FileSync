import os
import glob
import shutil
# from tkinter import *
# test



dirNames = ["Audio", "Documents", "Videos", "Images", "Executables", "Archives", "Other"]

for x in dirNames:
    if os.path.exists(x):
        print(f"Warning! Directory {x} already exists! Do you want to continue? Y/N")
        while True:
            temp = input()
            if temp.lower() == "y":
                break
            elif temp.lower() == "n":
                raise Exception("Directory already exists!")
            else:
                print("Choose the correct answer!")
                continue
    else:
        os.makedirs(x)

audioExtensions = ["mp3", "waw", "m4a", "flac", "wma", "aac"]
documentsExtensions = ["odt", "pdf", "xls", "xlsx", "ods", "ppt", "pptx", "txt", "epub", "mobi" ,"doc", "docx", "rtf"]
videosExtensions = ["mp4", "webm", "flv", "vob", "avi", "amv", "mpg", "mov"]
imagesExtensions = ["jpeg", "jpg", "tiff", "png", "bmp", "xcf", "psd", "flif", "gif"]
exeExtensions = ["exe", "msi"]
archivesExtensions = ["7z", "zip", "rar", "bz2", "gz", "ace", "tar"]

number = 0
for file in glob.glob("*.*"):
    temp = file.split('.')
    

    if temp[0] == "Organiser" and temp[1] == "exe":
        continue
    elif temp[1] in audioExtensions:
        shutil.move(file, "Audio")
        number += 1
    elif temp[1] in documentsExtensions:
        shutil.move(file, "Documents")
        number += 1
    elif temp[1] in videosExtensions:
        shutil.move(file, "Videos")
        number += 1
    elif temp[1] in imagesExtensions:
        shutil.move(file, "Images")
        number += 1
    elif temp[1] in exeExtensions:
        shutil.move(file, "Executables")
        number += 1
    elif temp[1] in archivesExtensions:
        shutil.move(file, "Archives")
        number += 1
    elif temp[1] != "py":
        shutil.move(file, "Other")
        number += 1

print(f"replacement finished! Moved {number} file(s).")
input()