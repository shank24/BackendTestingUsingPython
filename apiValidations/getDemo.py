import configparser
import requests

config = configparser.ConfigParser()
config.read('/home/shanky/PycharmProjects/backendTesting/utilities/properties.ini')

# url = "https://api.getpostman.com/collections"
headers = {"X-Api-Key": "PMAK-5fbc920d2e116d00438ba11a-0fbc28fc41915c6b7c533c28a9ec5132fd"}
response = requests.get(config['API']['endpoint'] + 'collections', headers=headers)

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
