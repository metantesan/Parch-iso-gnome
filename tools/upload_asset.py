from mega import Mega
import os
from os import listdir
from os.path import isfile, join

email=os.getenv("email")
password=os.getenv("password")
mega = Mega()
mega._login_user(email,password)
                 
def absoluteFilePaths(directory):
     for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))

directory = "out/"
file_path_generator = absoluteFilePaths(directory)

Folder = mega.find('parchlinux') #change it with the folder in your mega
for file_path in file_path_generator:
    mega.upload(file_path, Folder[0])
