#!/usr/bin/python3

import socket, threading
from util import *

class threads(Thread):
   def __init__(self, conn, addr):
      Thread.__init__(self)
      self.conn = conn
      self.addr = addr

   def run(self):
      with self.conn:
         print('Connected -> ', self.addr)
         tot = 0

         while True:
            line = (self.conn.recv(1024)).decode() #Receive and decode info
            
            if not line: break
            tot += read(line)
            var  = (str(tot)).encode()
            
            self.conn.sendall(var)
         print("Final Result THREAD %s-> %0.2f" %  (self.getName(), tot))
         
         
def connect(HOST, PORT):
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((HOST, PORT))

      while True:
         s.listen(1)
         
         try:
            conn, addr = s.accept()
            n_thread   = threads(conn, addr)
            print("Created THREAD nr -> %s" % n_thread.getName())
            n_thread.start()
            
         except:
            abort("\nClosing.")
            return


if __name__ == '__main__':
   HOST = ''
   PORT = 50009

   # Main function
   connect(HOST, PORT)
