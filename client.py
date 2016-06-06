#!/usr/bin/python3

import socket, sys, hashlib

def hash(line):
   m = hashlib.md5()
   m.update(line.encode())
   return m.digest()

def connect(HOST, PORT, FILE):
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      try:
         s.connect((HOST, PORT))
         a = str(HOST) + str(PORT)
         print(a)
         print(hash(a))
      except:
         print("Connection refused.")
         exit()
      


      with open(FILE, 'r') as f:
         for i in f:
            try:
               s.send(i.encode())
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
   print("Total -> ", connect('127.0.0.1', 50009, sys.argv[1]))


if __name__ == '__main__':
   main()