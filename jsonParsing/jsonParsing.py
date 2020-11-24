import json

courses = '{"name": "Shanky", "languages": ["Java","Python"]}'

#Loads Method parse and it returns dict.
dict_courses = json.loads(courses)

print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])
list_language = dict_courses['languages']
print(type(list_language))

for i in list_language:
    print(i)
