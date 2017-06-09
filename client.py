import socket
import json
from common import send_msg, recv_msg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                           

port = 9999
s.connect((host, port))                               

msg = "abs"#.encode('utf-8')

send_msg(s, msg)
data = recv_msg(s)

s.close()
print(data)