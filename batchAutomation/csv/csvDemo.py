import csv

with open('/home/shanky/PycharmProjects/backendTesting/utilities/file.csv', 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    #print(csvReader)
    #print(list(csvReader))
    name=[]
    status=[]
    for row in csvReader:
        name.append(row[0])
        status.append(row[1])

print(name)
print(status)

#Getting Index of list
index = name.index('Kim')
print(status[index])

#Write back to csvFile
#a for append from existing data
with open('/home/shanky/PycharmProjects/backendTesting/utilities/file.csv', 'a') as wFile:
    write = csv.writer(wFile)
    write.writerow(["Tob","Rejected"])

