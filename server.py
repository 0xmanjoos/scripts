#!/usr/bin/env python3
import socket, time, sys

class colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	END = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


banner = colors.OKBLUE+colors.BOLD+"""
  __     _____ _         _____      ______   _ _   _      
 / _|   |  ___| |       |  _  |     |  _  \ (_) \ | |     
| |_ ___| |__ | |   __ _| | | | ___ | | | |  _|  \| | ___ 
|  _/ _ \  __|| |  / _` | | | |/ _ \| | | | | | . ` |/ __|
| ||  __/ |___| | | (_| \ \_/ / (_) | |/ /  | | |\  | (__ 
|_| \___\____/|_|  \__, |\___/ \___/|___/   |_\_| \_/\___|
                    __/ |                                 
                   |___/     
                  LOGIN SYSTEM


"""+colors.END

def server(host, port):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((host, port))
	s.listen(5)
	conn, addr = s.accept()
	with conn:
		win = []
		conn.sendall(banner.encode('utf-8'))
		while True:
			conn.sendall(b"Password: ")
			data = conn.recv(1024)
			if not data:
				break
			if data.decode() == "password\n":
				congrats = colors.WARNING+colors.UNDERLINE+"\nCongrats! Here's your flag \n\n FLAG{95728ce2159815f2e2a253c664b2493f}\n\n" + colors.END
				conn.sendall(congrats.encode())
				win.append(addr)
				break
			else:
				error = colors.FAIL+colors.BOLD+"\nThats the wrong password!\n\n"+colors.END
				conn.sendall(error.encode("utf-8"))
				break
if __name__ == "__main__":
	try:
		print(banner + "\nSocket Server Running on Port 0.0.0.0:4444")
		while 1:
			server("0.0.0.0", 4444)
	except KeyboardInterrupt:
		print(colors.FAIL+colors.BOLD+"\nThank you for using FeelGood Inc. Login System"+colors.END)
