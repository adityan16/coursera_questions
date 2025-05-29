import urllib.request
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input the starting URL, count, and position
url = input("Enter URL: ").strip()
count = int(input("Enter count: ").strip())
position = int(input("Enter position: ").strip()) - 1  # Convert to 0-based index

# Loop through count times to follow the links
for i in range(count + 1):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position].get('href')
