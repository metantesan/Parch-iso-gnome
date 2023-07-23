from mega import Mega
import os
from os import listdir
from os.path import isfile, join

email=os.getenv("email")
password=os.getenv("password")
mega = Mega()
m = mega.login(email, password)
_path = list(Path().cwd().glob("out/*.iso"))[0]
path = _path.as_posix()
m.upload(path)
