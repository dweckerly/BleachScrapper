# waiting to get walmart API key to utilize for more price comparison...
import urllib.request, json

with urllib.request.urlopen("http://api.walmartlabs.com/v1/items?apiKey=dg2qjj742ydv4krde9mkxg6v&upc=035000521019") as url:
    data = json.loads(url.read().decode())
    string = [x.strip() for x in str(data['items']).split(',')]
    print(string[2])
