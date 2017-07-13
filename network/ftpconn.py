import ftplib
import atexit

Transfer = ftplib.FTP("","","")

ADDRESS = USERNAME = PASSWORD = ""

def init_creditinals(addr,usr,pssd):
    global ADDRESS,USERNAME,PASSWORD,Transfer
    ADDRESS = addr
    USERNAME = usr
    PASSWORD = pssd
    try:
        Transfer = ftplib.FTP(ADDRESS,USERNAME,PASSWORD)
    except:
        init_creditinals(ADDRESS,USERNAME,PASSWORD)

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
                          