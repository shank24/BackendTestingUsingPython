import requests, json, jsonpath

# URL
url = "https://reqres.in/api/users"


def test_create_new_user():
    # Read Input Json File
    file = open("/home/shanky/PycharmProjects/backendTesting/File/CreateUser.json", 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    # Make POST request with Json Payload
    response = requests.post(url, request_json)
    print(response.content)
    # Validating Response Code
    assert response.status_code == 201
    # Fetch Header from Response
    print('Content-Length ', response.headers.get('Content-Length'))
    # Parse response into Json Format
    response_json = json.loads(response.text)
    # Pick Id using Json Path
    id = jsonpath.jsonpath(response_json, 'id')
    print('ID', id[0])
