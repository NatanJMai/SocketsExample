import socket, sys

def connect(HOST, PORT, FILE):
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      try:
         s.connect((HOST, PORT))
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
   print(sys.argv[1])
   print("Total -> ", connect('localhost', 50009, sys.argv[1]))

if __name__ == '__main__':
   main()
