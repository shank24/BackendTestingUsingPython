import requests

url = 'https://petstore.swagger.io/v2/pet/9843217/uploadImage'
files = {'file' : open('/home/shanky/Downloads/mine.jpg' , 'rb')}

response = requests.post(url,files=files)
print(response.status_code)
print(response.text)