import os
import tkinter as tk
from tkinter.filedialog import askdirectory

root = tk.Tk()
root.withdraw()

dir_path = askdirectory()

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file == '.DS_Store':
            print(root, file)
            flag = input("Delete?")
            if flag == "Y":
                os.remove(file)