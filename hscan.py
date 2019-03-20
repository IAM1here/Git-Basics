#!/usr/bin/python
import requests
import argparse
import threading
import time
def mandate():
    print """ 
            NOTE: IF FAIL ERROR APPEARS COUPLE OF RUNS, WAIT FOR SOME TIME AS MAX TRIES REACHES
                  IT THROWS CONNECTION REFUSED

       """

def banner():
    print """
            _   _  ___   ___    __    _  _ 
           ( )_( )/ __) / __)  /__\  ( \( )
            ) _ ( \__ \( (__  /(__)\  )  ( 
           (_) (_)(___/ \___)(__)(__)(_)\_)
            
            WELCOME TO HTTP IP RANGE SCANNER
                                  ~ ASHISH JHA



            COMMAND: hscan.py -a 192.168.43.145
                     hscan.py --address 10.0.0.1
"""

def ipResponse(iprange,i):
              try:
                response=requests.get("http://" + iprange + "." + str(i) )
                data= response.headers['server'] if 'server' in response.headers else "Returned none"
                print "[+] Response Received " + iprange+"." +str(i) + "\tStatus_code:"+ str(response.status_code) + "\tServer:" + data +"\n"
              except requests.exceptions.ConnectionError :
                 print "[!] CONNECTION REFUSED " + iprange+ "." + str(i) +"\n"
               
def main():
    args=argparse.ArgumentParser("hscan.py")
    args.add_argument("-a","--address",type=str,help="Specify the ip address for the range to be scanned!")
    args.add_argument("-sc","--scode",type=str,help="Specify the status codes which you want the result for",)
    parser=args.parse_args()
    iprange=parser.address
    if iprange  == None:
            banner()
            exit()
    data = [iprange[:i] for i in range(0,len(iprange)) if "." in iprange[i]]
    mandate()
    time.sleep(5)
    for i in range(0,255):
           p1 = threading.Thread(target=ipResponse, args=(data[2],i))
           p1.start()
    
if __name__ == "__main__":
                           main()
