import socket

def abort(msg):
   print(msg)
   exit()

def read(line):
   tot = 0
   spl = line.split()

   if spl != []: tot = float(spl[1]) * float(spl[2])
   return tot

def connect(HOST, PORT):
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((HOST, PORT))

      while True:
         s.listen(1)
         
         try:
            conn, addr = s.accept()
         except:
            abort("\nClosing.")
            return

         with conn:
            print('Connected by ', addr)

            tot = 0.0

            while True:
               rcve = (conn.recv(1024)).decode() #Receive and decode info
               
               if not rcve: break

               tot += read(rcve)
               conn.sendall(rcve.encode())
            print("Final Result-> ", tot)


if __name__ == '__main__':
   HOST = ''
   PORT = 50008

   # Main function
   connect(HOST, PORT)
