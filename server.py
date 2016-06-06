#!/usr/bin/python3

from util import *
import time

class threads(Thread):
   def __init__(self, conn, addr):
      Thread.__init__(self)
      self.conn = conn
      self.addr = addr

   def run(self):
      with self.conn:
         a = str(self.addr[0]) + str(PORT)
         r = hashlib.sha512(a.encode())

         print(r.digest())
         
         #print('Connected -> ', self.addr)

         tot = 0
         print(time.ctime())
         while True:
            line = (self.conn.recv(1024)).decode() #Receive and decode info
            
            if not line: break
            tot += read(line)
            var  = (str(round(tot, 2))).encode()
            self.conn.sendall(var)
         print(time.ctime())
         print("\n######################\nFinal Result THREAD %s-> %0.2f" %  (self.getName(), tot))
         
         
def connect(HOST, PORT):
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((HOST, PORT))

      while True:
         s.listen(1)
         
         try:
            conn, addr = s.accept()
            n_thread   = threads(conn, addr)
            print("\n----------------------\nCreated THREAD nr -> %s" % n_thread.getName())
            n_thread.start()
            
         except:
            abort("\nClosing.")
            return


if __name__ == '__main__':
   HOST = 'localhost'
   PORT = 50009

   # Main function
   connect(HOST, PORT)
