import requests
from utilities.configurations import getConfig,getHeaders
from utilities.resources import APIResource

url = getConfig()['API']['endpoint'] + APIResource.getCollectionId
response = requests.get(url, headers=getHeaders())

json_response = response.json()
print(type(json_response))

print(json_response['user'])

#print(json_response['operations'][2]['name'])

var = len(json_response['operations'])

i=0
for res in json_response['operations']:
    if json_response['operations'][i]['name'] == 'mock_usage':
        print('Found Matched !!! ')
        print(json_response['operations'][i]['limit'])
        break
    i=i+1

