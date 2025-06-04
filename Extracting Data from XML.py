import urllib.request
import xml.etree.ElementTree as ET

# Prompt for URL
url = input('Enter location: ')
print('Retrieving', url)

# Open the URL and read the data
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')

# Parse XML from the data
tree = ET.fromstring(data)

# Find all count tags under any comment
counts = tree.findall('.//count')

# Calculate total count and sum
total = 0
for count in counts:
    total += int(count.text)

print('Count:', len(counts))
print('Sum:', total)
