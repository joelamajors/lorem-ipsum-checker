from bs4 import BeautifulSoup
import re
import requests

links = []
pages = []

lorem = set()

lorem_string = "Lorem ipsum dolor amet consectetur adipiscing elit sed eiusmod tempor incididunt ut labore dolore magna aliqua Ut enim minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ea commodo consequat Duis aute irure dolor reprehenderit voluptate velit esse cillum dolore fugiat nulla pariatur Excepteur sint occaecat cupidatat proident sunt culpa qui officia deserunt mollit anim laborum".split()

for w in lorem_string:
    lorem.add(w)

#opens urls
f = open('urls.txt', 'r')

for line in f:

    # Removing new line from lines
    line = line.rstrip('\n')

    # Go to URL
    req = requests.get(line)
    soup = BeautifulSoup(req.content, 'html.parser')
    req.close()


    # If text has has Lorem Ipsum,
    for l in lorem:
        if soup.find(string=re.compile(" " + l + " " ,re.IGNORECASE)):
            pages.append(line)

for p in pages:
    if p not in links:
        links.append(p)

print("These links have Lorem Ipsum:")
print('\n'.join(map(str,links)))

f.close()
