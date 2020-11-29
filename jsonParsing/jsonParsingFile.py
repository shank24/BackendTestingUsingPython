import json,jsonpath

#Parse content present in Json File

with open('/home/shanky/PycharmProjects/backendTesting/jsonParsing/jsonfile.json') as f:
    data = json.load(f)
    #print(data)
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])

#Price of a course RPA
    #print(data['courses'][2]['price'])
    for course in data['courses']:
        if course['title'] == "RPA":
            print(course['price'])
            assert course['price'] == 500