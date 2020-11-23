import requests,json,jsonpath
#URL
url="https://reqres.in/api/users/2"

def test_put_resource():
        #Read Input Json File
        file =open("File/CreateUser.json", 'r')
        json_input= file.read()
        #Parsing into Json
        request_json = json.loads(json_input)
        print(request_json)
        #Make PUT request with Json Payload
        response = requests.put(url, request_json)
        print(response.content)
        #Validating Response Code
        assert response.status_code == 200
        #Parse Response Content
        response_json = json.loads(response.text)
        updated = jsonpath.jsonpath(response_json,'updatedAt')
        print(updated)