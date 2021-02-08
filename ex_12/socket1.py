# SIMPLE WEB BROWSER

# import socket module
import socket

# create socket obj
# socket.socket(family=AF_INET, type=SOCK_STREAM, protocol=0, fileno=None)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to remote socket address on port 80
s.connect(('data.pr4e.org', 80))
# GET request followed by blank line (\r\n\r\n), and encoded req into bytes
req = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# send request to socket connection
s.send(req)

while True:
  # keep receiving bytes(data) 512 byte chunks at a time from socket end
  data = s.recv(512)
  # when no more bytes are being received, no more data is received from this connection
  if len(data) < 1:
    break
  # print out the decoded bytes to string and end each line with an empty '' instead of '\n'
  print(data.decode(), end='')

# close socket connection
s.close()