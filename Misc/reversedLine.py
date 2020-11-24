#The advantage of using with,
# is we do not have to use file.close()

with open('file.txt','r') as reader:
    content = reader.readlines()
    with open('file.txt','w') as writer:
        for line in reversed(content):
            print(line)



