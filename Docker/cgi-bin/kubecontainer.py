#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
name = mydata.getvalue("name")
image = mydata.getvalue("image")
#print(vol)
#print(mount)

if (name and image)==None:
        output2 = " Deploymnet Name or Image Name is missing"

else:
        cmd2 = "kubectl create deployment {0} --image {1}".format(name,image)
        output2 = subprocess.getoutput(cmd2)

print(output2)

 
