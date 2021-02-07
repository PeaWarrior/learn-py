# Exercise 3: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195


try :
  userInput = input('Enter a file name: ')
  fileHandler = open(userInput)
  emailCount = {}
  maxCount = 0
  maxEmail = None

  for line in fileHandler :
    if line.startswith('From: ') :
      line = line.split()
      email = line[1]
      emailCount[email] = emailCount.get(email, 0) + 1

  def callback(email) :
    return emailCount[email]

  maxEmailCount = max(emailCount, key=callback)
  print(maxEmailCount, emailCount[maxEmailCount])
except :
  print("Can't find file")