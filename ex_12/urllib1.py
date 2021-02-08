# import urllib library request method
import urllib.request

# urllib request and urlopen returns a fileHandle like object without the headers
fileHandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# interate through each line and print out the decoded bytes
for line in fileHandle:
  print(line.decode().strip())