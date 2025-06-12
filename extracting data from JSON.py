import json
import urllib.request, urllib.parse
import http, json, ssl

service_url = "http://py4e-data.dr-chuck.net/comments_2218194.json"

data = urllib.request.urlopen(service_url).read().decode()

print("Retrieved", len(data), "characters")

# Parse the JSON
info = json.loads(data)

# Extract the list of comments
comments = info['comments']

# Sum up all the 'count' values
total = sum(item['count'] for item in comments)

print("Count:", len(comments))
print("Sum:", total)
