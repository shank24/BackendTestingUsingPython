import requests
from bs4 import BeautifulSoup

li = []
data = requests.get('https://rahulshettyacademy.com/AutomationPractice/')
soup = BeautifulSoup(data.content, 'html.parser')
#print(soup.prettify())
table = soup.find('table', {'class': 'table-display'})

row_data = table.find_all('tr')
for row in row_data:
    if row.find_all('td'):
        columns = row.find_all('td')
        print(columns[1])












#Visible Text
appium = soup.find('a',string='Appium')
print(appium['href'])
