#!/usr/bin/python3

# NatanJMai
# github.com/@NatanJMai

import socket, sys, hashlib
from Crypto.Cipher   import AES
from Crypto          import Random 

def hash(HOST, PORT):
   m = hashlib.sha256((str(HOST) + str(PORT)).encode())
   return m.digest()[0:16]


def crypt(line, r):
   aes  = AES.new(r, AES.MODE_CFB, r) 
   data = line.encode('utf-8') 
   data = aes.encrypt(data) 
   return data
  

def connect(HOST, PORT, FILE):
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      try:
         s.connect((HOST, PORT))
      except:
         print("Connection refused.")
         exit()
      
      with open(FILE, 'r') as f:
         m = hash(HOST, PORT)
         for i in f:
            try:
               c = crypt(i, m)         
               print("Send -> %s" % (c))
               s.send(c)
               data = s.recv(1024)
            except:
               print("Send fail!")
               exit()
         
         sumt = float(data.decode())
         
         f.close()
         s.close()
   return sumt
      

def main():
   print("Loading...")
   total = connect('localhost', 50009, sys.argv[1])

   print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
   print("| Total -> ", total)
   print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


if __name__ == '__main__':
   main()