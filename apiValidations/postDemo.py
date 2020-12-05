import requests
from utilities.configurations import getConfig, getHeaders, getRandomNumber
from utilities.resources import APIResource

from payload.postPayload import addCollectionPayload

url = getConfig()['API']['endpoint'] + APIResource.createCollection

#Creating a collection
post_response = requests.post(url, json=addCollectionPayload("Sample"+str(getRandomNumber())), headers=getHeaders())

print(post_response.status_code)
#Converting it into json
response_json = post_response.json()
print(response_json['collection']['uid'])
uid = response_json['collection']['uid']

#Deleting a collection
delete_response = requests.delete(url + "/"+uid, headers=getHeaders())

print(delete_response.status_code)