#!/usr/bin/env python3

#for file dialog windows
from tkinter import Tk
from tkinter.filedialog import askdirectory

#to generate list of all files in folder
import os

dSelect = askdirectory()

print(dSelect)

#creates dummy file for renameing process
try:
    path = f'{dSelect}/renameMe.txt'
    isExist = os.path.exists(path)
    print(isExist)
    open(f'{dSelect}/renameMe.txt','w')
except:
    print('file already exists')


#run to create updated file list
file_list = os.listdir(dSelect)
print(file_list)
count = 0
for file in file_list:
    count = count+1
    #check for file extention
    if file.endswith('.txt'):
        #check if 'rename' is in the file name
        if 'rename' in file:
            #replace renameMe with iWasRenamed
            newName = file.replace('renameMe',f'iWasRenamed{count}')
            #rename the file using os.rename
            os.rename(os.path.join(dSelect,file), os.path.join(dSelect, newName))
            # print out confirmation
            print(f"Renamed {file} to {newName}")