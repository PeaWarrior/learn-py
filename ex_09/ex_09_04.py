# Exercise 4: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

userInput = input('Enter a file name: ')
fileHandler = open(userInput)
domainNames = {}

for line in fileHandler :
  if line.startswith('From ') :
    atSymbolIndex = line.find('@')
    endDomainIndex = line.find(' ', atSymbolIndex)
    domainName = line[atSymbolIndex + 1 : endDomainIndex]
    domainNames[domainName] = domainNames.get(domainName, 0) + 1
  
print(domainNames)