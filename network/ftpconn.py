import ftplib
import atexit

Transfer = ftplib.FTP("","","")

ADDRESS = USERNAME = PASSWORD = ""

def init_creditinals(addr,usr,pssd):
    global ADDRESS,USERNAME,PASSWORD,Transfer
    ADDRESS = addr
    USERNAME = usr
    PASSWORD = pssd
    Transfer = ftplib.FTP(ADDRESS,USERNAME,PASSWORD)

def OnScriptEnd():
    print("Script ending")
    Transfer.quit()

def upload_to_ftp(name,upname,mode):
    file = open(name,mode)   
    Transfer.storbinary('STOR ' + upname , file)    
    file.close()
                          