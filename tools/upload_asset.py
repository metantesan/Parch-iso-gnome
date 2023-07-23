
import os
email=os.getenv("email")
password=os.getenv("password")
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
_path = list(Path().cwd().glob("out/*.iso"))[0]
path = _path.as_posix()
# create an instance of the API class
api_instance = swagger_client.FileUploadApi()
apiecoKey = apiecoKey_example # String | 
expiry = "4 w" # String | The query param expires must be a positive integer which, by default, represents the number of days until the file will be deleted (defaults to 14 days). If you follow it with w, it will be the number of weeks. m for months and y for years. (optional)
file = path # File |  (optional)

try: 
    # Upload File
    api_response = api_instance.upload_file(apiecoKey, expiry=expiry, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileUploadApi->uploadFile: %s\n" % e)

