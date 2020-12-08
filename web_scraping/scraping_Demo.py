import requests
from bs4 import BeautifulSoup

li = []
data = requests.get('https://www.imdb.com/find?s=ep&q=Thriller&ref_=nv_sr_sm')
soup = BeautifulSoup(data.content, 'html.parser')
# print(soup.prettify())
table = soup.find('table', {'class': 'findList'})
#print(table.prettify())

row_data = table.find_all('tr')
for row in row_data:
    columns = row.find_all('td')
    #print(columns[1].a.text)
    suburl = columns[1].a['href']
    subdata = requests.get('https://www.imdb.com'+suburl)
    childSoup = BeautifulSoup(subdata.content, 'html.parser')
    if childSoup.find('div',{'class':'see-more inline canwrap'}):
        genre = childSoup.find('div',{'class':'see-more inline canwrap'})
        if genre.a.text == ' Documentary':
            #print(columns[1].a.text)
            #print(genre.a.text)
            li.append(columns[1].a.text)


print(li)