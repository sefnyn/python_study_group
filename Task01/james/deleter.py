import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

dir_path = filedialog.askopenfilename()

for root, dirs, files in os.walk(dir_path):
    os.chdir(root)
    for file in files:
        if file == '.DS_Store':
            print(root, file)
            os.remove(file)