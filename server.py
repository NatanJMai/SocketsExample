#!/usr/bin/python3

# NatanJMai
# github.com/NatanJMai/SocketsExample

from util import *
import time, sys

class threads(Thread):
   def __init__(self, conn, addr):
      Thread.__init__(self)
      self.conn = conn
      self.addr = addr

   def run(self):
      with self.conn:
         print('Address -> ', self.addr)
         
         tot = 0
         has = hash(HOST, PORT)
         #print("\nTIME Start - %s\n" % time.ctime())
         while True:
            encpt = self.conn.recv(1024) #Receive and decode info
            dcptd = decrypt(encpt, has)
            #print("Rcve -> %s | %s" % (encpt, dcptd))

            if not dcptd: break
            tot += read(dcptd)
            var  = (str(round(tot, 2))).encode()
            self.conn.sendall(var)

         print("TIME End - Thread %s %s" % (time.ctime(), self.getName()))
         print('----------------------\n')
         
         
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
   HOST = sys.argv[1]
   PORT = int(sys.argv[2])

   # Main function
   connect(HOST, PORT)
