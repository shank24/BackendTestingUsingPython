import requests,json,jsonpath

#API URL
url ="https://reqres.in/api/users?page=2"

def test_getUserData():
        #Send Get Request
        response = requests.get(url)
        #Display Response Content
        # print (json.dumps(response.json(), indent=4, sort_keys=True))
        #Parse Response to JSON Format
        json_response = json.loads(response.text);
        #print(json_response)
        #Fetch value using JSONPath
        pages = jsonpath.jsonpath(json_response,'total_pages')
        print(pages[0])
        assert pages[0]==2