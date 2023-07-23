from pathlib import Path

import os
email=os.getenv("email")
password=os.getenv("password")

_path = list(Path().cwd().glob("out/*.iso"))[0]
path = _path.as_posix()
import ftplib
session = ftplib.FTP('shatel2.parsaspace.com',email,password)
file = open(path,'rb')                  # file to send
session.storbinary('STOR iso.iso', file)     # send the file
file.close()                                    # close file and FTP
session.quit()
