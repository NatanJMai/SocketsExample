#!/usr/bin/python

import socket, threading
from util import *

class threads(Thread):
   def __init__(self):
      Thread.__init__(self)

   def run(self, conn, addr, tot):
      with conn:
         print('Connected by ', addr)

         while True:
            line = (conn.recv(1024)).decode() #Receive and decode info
            
            if not line: break
            tot += read(line)
            var  = (str(tot)).encode()
            
            conn.sendall(var)

         print("Final Result THREAD %s -> %0.2f" %(self.getName, tot))


def connect(HOST, PORT):
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((HOST, PORT))

      while True:
         tot = 0.0
         s.listen(1)
         
         try:
            conn, addr = s.accept()
         except:
            abort("\nClosing.")
            return

         n_thread   = threads()
         n_thread.run(conn, addr, 0)


if __name__ == '__main__':
   HOST = ''
   PORT = 50009

   # Main function
   connect(HOST, PORT)
