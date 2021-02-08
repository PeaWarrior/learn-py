# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195

userInput = input('Enter a file name: ')
fileHandler = open(userInput)
commits = {}

for line in fileHandler :
  if line.startswith('From ') :
    line = line.split()
    email = line[1]
    commits[email] = commits.get(email, 0) + 1

commitsList = []
for email, count in list(commits.items()) :
  commitsList.append((count, email))

commitsList.sort(reverse = True)

print(commitsList[0][1], commitsList[0][0])