import urllib.request, json

class WalmartAPI:
    def __int__(self, api='dg2qjj742ydv4krde9mkxg6v'):
        self._api = api

    def api(self, a=None):
        if a: self._api = a
        return self._api

def get_data(req):
    data = json.loads(req.read().decode())
    return data 

def search_request(term):
    req = urllib.request.urlopen(f"http://api.walmartlabs.com/v1/search?apiKey=dg2qjj742ydv4krde9mkxg6v&query={term}")
    get_data(req)

def upc_request(upc):
    req = urllib.request.urlopen(f"http://api.walmartlabs.com/v1/items?apiKey=dg2qjj742ydv4krde9mkxg6v&upc={upc}")
    get_data(req)