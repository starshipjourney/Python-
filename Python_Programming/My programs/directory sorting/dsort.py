#!/usr/bin/env python3
import os
import shutil
import pathlib

def sort(our_path,working_dir):
    files = os.listdir(working_dir)
    all_extensions =[]
    for i in files:
        file_extension = pathlib.Path(i).suffix
        if file_extension:
            all_extensions.append((i,file_extension))
    # print(all_extensions)

    for f,e in all_extensions: #f for file , e for extension
        file_loc = os.path.join(our_path,f)
        try:
            os.mkdir(e[1:])
            new_folder_loc = os.path.join(our_path,e[1:])
            shutil.move(file_loc, new_folder_loc)
        except:
            new_folder_loc = os.path.join(our_path,e[1:])
            shutil.move(file_loc, new_folder_loc)

    print("DIRECTORY SORTED")
    
#--------MAIN---------------------------------------------------------------------------------------------------------------------------------------
our_path = input("Enter path of directory to sort")
try:
    working_dir = os.chdir(our_path)
except:
    print(">>>  Path is invalid  <<<")
    exit() 
sort(our_path,working_dir)