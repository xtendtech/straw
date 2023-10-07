import os
import zipfile
print(os.getcwd())
try:
    os.mkdir("zip")
except Exception as E  :
     print(E)

with zipfile ('one.zip','w') as myzip:
     myzip.write("hello")
     
    
    