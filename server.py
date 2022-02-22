import socket



s = socket.socket()

s.bind(('localhost', 42212))

s.listen(5)


c, addr = s.accept()


c.send('Thank you for connecting'.encode())
print(c.recv(6).decode())


while True:
	c.send("2".encode())
	cmd = input(c.recv(100).decode()[:-1] + " > ")
	c.send(cmd.encode())
	print(c.recv(1024).decode())



c.close()




