import requests
#API URL
url ="https://reqres.in/api/users/2"

def test_delete_user():
        response = requests.delete(url)
        #Fetch Response Code
        statusCode=response.status_code
        print(statusCode)
        assert statusCode == 204

