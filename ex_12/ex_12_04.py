# Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document and display the count of the paragraphs as the output of your program. Do not display the paragraph text, only count them. Test your program on several small web pages as well as some larger web pages.
# http://dr-chuck.com/dr-chuck/resume/bio.htm

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter URL: ')
html = urlopen(url)

soup = BeautifulSoup(html, 'html.parser')
print('Number of p tags:', len(soup.find_all('p')))