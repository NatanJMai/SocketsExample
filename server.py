import socket

HOST = ''
PORT = 50008

def read(line):
	pass

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))

	while True:
		s.listen(1)
		conn, addr = s.accept()
		
		with conn:
			print('Connected by ', addr)
			while True:
				rcve = (conn.recv(1024)).decode() #Receive and decode info
				print(rcve)
				
				read(rcve)
				
				if not rcve: break
				conn.sendall(rcve.encode())
