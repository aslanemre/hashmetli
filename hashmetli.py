#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import hashlib
import time
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
from getpass import getpass
def logo():
	print("""
		         __    _                                   
                    _wr""        "-q__                             
                 _dP                 9m_     
               _#P                     9#_                         
              d#@  Project: Hashmetli   9#m                        
             d##                         ###                       
            J###                         ###L                      
            {###K                       J###K                      
            ]####K      ___aaa___      J####F                      
        __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
     _g##############mZ_         __g##############m_               
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
  a###""          ,Z"#####@" '######"\g          ""M##m            
 J#@"             0L  "*##     ##@"  J#              *#K           
 #"               `#    "_gmwgm_~    dF               `#_          
7F                 "#_   ]#####F   _dK                 JE          
]                    *m__ ##### __g@"                   F          
                       "PJ#####LP"                                 
 `                       0######_                      '           
                       _0########_                                   
     .               _d#####^#####m__              ,              
      "*w_________am#####P"   ~9#####mw_________w*"                  
          ""9@#####@M""           ""P@#####@M""                    
""")
print("")
logo()
passwd = "hashmetli"
secim = input(" [?] Encrypt - 1 Decrypt - 2 = ")
os.system("clear")
logo()
if secim == "1":
	text = input(" [?] Text : ")
	encrypted1 = encrypt(passwd, text)
	encrypted2 = b64encode(encrypted1)
	print(" [+] Şifrelendi : ", encrypted2)
if secim == "2":
	text = input(" [?] Text : ")
	decrypted1 = b64decode(text)
	decrypted2 = decrypt(passwd, decrypted1)
	print(" [+] Şifre Çözüldü : ", decrypted2)
