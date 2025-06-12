import urllib.request, urllib.parse
import json, ssl

service_url = "http://py4e-data.dr-chuck.net/opengeo?"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("ENTER THE LOCATION : ")
    if address is None:
        break

    address = address.strip()
    params = dict()
    params['q'] = address
    url = service_url + urllib.parse.urlencode(params)
    print(f"Retrieving from {url}")
    uh = urllib.request.urlopen(url, context = ctx)
    data = uh.read().decode()
    print(f"Retrieving {len(data)}, characters {data[:20].replace('\n', ' ')}")
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'features' not in js:
        print("Dowlnoad Error.....")
        print(data)
        break
    if len(js['features']) == 0:
        print("Object not found.....")
        print(data)
        break
    props = js['features'][0]['properties']
    lat = props.get('lat')
    lon = props.get('lon')
    location = props.get('formatted')
    plus_code = props.get('plus_code')  
    print(f"lat: {lat}, lon: {lon}")
    print("Location:", location)
    print("Plus code:", plus_code)
