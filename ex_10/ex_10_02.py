# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

userInput = input('Enter a file name: ')
fileHandler = open(userInput)
hourCount = {}

for line in fileHandler:
  if line.startswith('From '):
    line = line.split()
    time = line[5]
    time = time.split(':')
    hour = time[0]
    hourCount[hour] = hourCount.get(hour, 0) + 1

hourCountsList = []
for hour, count in list(hourCount.items()):
  hourCountsList.append((hour, count))

hourCountsList.sort()

for hour, count in hourCountsList:
  print(hour, count)