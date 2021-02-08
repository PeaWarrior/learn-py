# Exercise 2: Write a program to look for lines of the form:

# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

# Enter file:mbox.txt
# 38549

# Enter file:mbox-short.txt
# 39756

import re

userInput = input('Enter file: ')
fileHandle = open(userInput)

lines = fileHandle.read()
revisions = re.findall('New Revision:\s([0-9]+)', lines)

total = 0
for revision in revisions:
  total = total + int(revision)

average = int(total/len(revisions))

print(average)