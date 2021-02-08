# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

import socket

try:
  url = input('Enter a URL: ')
  host = url.split('/')[2]
  print(host)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host, 80))
  req = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
  s.send(req)

  received = b''
  while True:
    data = s.recv(512)
    if len(data) < 1:
      break
    received += data
  received = received.decode()
  print(received[:3000])
  print('Total number of characters:', len(received))
except:
  print('URL improperly formatted or non-existent URL')