import ctypes  
import os  
import pyhk

def fun():
    print "Do something"



def capture():  
    try:  
        dll = ctypes.cdll.LoadLibrary('PrScrn.dll')  
    except Exception:  
        print("Dll load error!")  
        return  
    else:  
        try:  
            dll.PrScrn(0)  
        except Exception:  
            print("Sth wrong in capture!")  
            return  
  
def main():  
    capture()   
  
if __name__ == "__main__":  
   #create pyhk class instance
	hot = pyhk.pyhk()

	#add hotkey
	hot.addHotkey(['F9'],fun)

	#start looking for hotkey.
	hot.start()