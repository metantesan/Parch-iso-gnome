from mega import Mega
import os
from os import listdir
from os.path import isfile, join

email=os.getenv("email")
password=os.getenv("password")
mega = Mega()
m = mega.login(email, password)
filename = "data.csv"
m.upload(filename)
