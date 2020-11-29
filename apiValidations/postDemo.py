import requests

from payload.postPayload import addCollectionPayload

url = "https://api.getpostman.com/collections"
headers = {"X-Api-Key": "PMAK-5fbc920d2e116d00438ba11a-0fbc28fc41915c6b7c533c28a9ec5132fd",
           "Content-Type": "application/json"}

#Creating a collection
post_response = requests.post(url, json=addCollectionPayload(), headers=headers)
print(post_response.status_code)
#Converting it into json
response_json = post_response.json()
print(response_json['collection']['uid'])
uid = response_json['collection']['uid']

#Deleting a collection

delete_response = requests.delete(url+"/"+uid, headers=headers)

print(delete_response.status_code)