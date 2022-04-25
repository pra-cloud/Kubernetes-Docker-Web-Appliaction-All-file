#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
dname = mydata.getvalue("dname")
scale = mydata.getvalue("scale")
#print(vol)
#print(mount)

if (dname and scale)==None:
        output2 = "Deployment Name or Scale Number is missing"

else:
        cmd2 = "kubectl scale deployment {0} --replicas {1}".format(dname,scale)
        output2 = subprocess.getoutput(cmd2)

print(output2)

 
