import requests
from utilities.configurations import getConfig,getHeaders
from utilities.resources import APIResource

url = getConfig()['API']['endpoint'] + APIResource.getCollection
response = requests.get(url, headers=getHeaders())

# print(response.content)
# print(response.status_code)
# print(type(response.text))
#
# dict_response=json.loads(response.text)
# print(dict_response['collections'][0]['id'])

#Simple ways
json_response = response.json()
print(type(json_response))
print(json_response['collections'][0]['id'])

assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
print(response.cookies)
