import urllib.request
import json

base_url = 'http://anapioficeandfire.com/api/'
endpoint = 'characters/583'

def get_response(url):
    print(url)
    with urllib.request.urlopen(url) as response:
        return response.read()


url = 'http://www.anapioficeandfire.com/api'
res = get_response(url)
prin(json.loads(res))
