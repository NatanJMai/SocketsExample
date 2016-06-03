import socket
from util import *


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

         with conn:
            print('Connected by ', addr)

            while True:
               line = (conn.recv(1024)).decode() #Receive and decode info
               
               if not line: break
               tot += read(line)
               var  = (str(tot)).encode()
               
               conn.sendall(var)


            
            print("Final Result-> ", tot)


if __name__ == '__main__':
   HOST = ''
   PORT = 50009

   # Main function
   connect(HOST, PORT)
