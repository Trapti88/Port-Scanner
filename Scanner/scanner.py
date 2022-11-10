##*** Author Trapti (Aliya) Meshram
#Date 11/10/2022 time 02 : 08 PM

import socket
import subprocess 
import sys
from datetime import datetime

#Using port banner,, but don't like:

subprocess.call("clear", shell=True)

#Ask which port do you want to Scan??

remoteServer=int(input("Enter a remote host to scan : "))
remoteServerIP = socket.gethostbyname(remoteServer)

print("Please wait, scanning remote host", remoteServerIP)

d1=datetime.now()

try: 
    for port in range(1,65535):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=s.connect_ex((remoteServerIP,port))
        if result == 0:
            print("Port {} :     open".format(port))
        s.close()    
      
except KeyboardInterrupt:
    print("You Press Ctrl+C")
    sys.ext()

except socket.gaierror:
    f"Hostname could not be resolved. Exiting"
    sys.exit()

#Checking Again
d2=datetime.now()

#Calculate the diffrence in time to know how long the scan took
total= d2- d1

#Printing the information on the screen  

f"Scanning completed in : ", total 




