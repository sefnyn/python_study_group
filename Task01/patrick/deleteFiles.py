#for file dialog windows
from tkinter import Tk
from tkinter.filedialog import askdirectory

#to generate list of all files in folder
import os

dir_path = askdirectory()
os.chdir(dir_path)

#creates dummy file for delete process
try:
    path = f'{dir_path}/thumbs.db'
    isExist = os.path.exists(path)
    print(path)
    print(isExist)
    open(f'{dir_path}/thumbs.db','w')
except:
    print('file already exists')

for item in os.listdir():
    if os.path.isfile(item):
        if item == 'thumbs.db': #file to remove
            print(item)
            os.remove(item)    