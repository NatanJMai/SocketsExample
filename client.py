import socket

def connect(HOST, PORT, FILE):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((HOST, PORT))

   f = open(FILE, 'r')

   for i in f:
      s.send(i.encode())
      data = s.recv(1024)
      print("rcv ", repr(data))
   f.close()
   s.close()


def main():
   connect('localhost', 50008, "file.txt")

if __name__ == '__main__':
   main()