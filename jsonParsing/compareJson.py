import jsonpath,json

#Parse content present in Json File1

with open('/home/shanky/PycharmProjects/backendTesting/jsonParsing/jsonfile.json') as f1:
    data1 = json.load(f1)

with open('/home/shanky/PycharmProjects/backendTesting/jsonParsing/jsonfile1.json') as f2:
    data2 = json.load(f2)
    print(data1 == data2)




