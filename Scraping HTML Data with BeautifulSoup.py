import urllib.request
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt for URL
url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
tags = soup('span')

# Sum the contents of the span tags
count = 0
total = 0

for tag in tags:
    try:
        num = int(tag.contents[0])
        total += num
        count += 1
    except:
        continue

# Output the results
print("Count", count)
print("Sum", total)




# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")

# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     # Look at the parts of a tag
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)
