from bs4 import BeautifulSoup
import re
import requests

#opens urls
f = open('urls.txt', 'r')

for line in f:

    # Removing new line from lines
    line = line.rstrip('\n')

    # print("\nChecking " + line)

    # Go to URL
    req = requests.get(line)
    soup = BeautifulSoup(req.content, 'html.parser')
    req.close()

    # If text has has Lorem Ipsum, 
    if soup.find(string=re.compile("lorem",re.IGNORECASE)):
        print('\nThese links have lorem ipsum: ')
        print(line)

f.close()