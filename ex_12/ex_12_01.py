# Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page. You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.
# http://data.pr4e.org/romeo-full.txt
# http://data.pr4e.org/romeo.txt
import socket

try:
  url = input('Enter a URL: ')
  host = url.split('/')[2]
  print(host)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host, 80))
  req = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
  s.send(req)

  while True:
    data = s.recv(512)
    if len(data) < 1:
      break
    print(data.decode(), end='')
except:
  print('URL improperly formatted or non-existent URL')