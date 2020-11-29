import requests, json

url = "https://api.getpostman.com/me"
headers = {"X-Api-Key": "PMAK-5fbc920d2e116d00438ba11a-0fbc28fc41915c6b7c533c28a9ec5132fd"}
response = requests.get(url, headers=headers)

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

