import requests

url = 'https://httpbin.org/cookies'
url1 = 'http://rahulshettyacademy.com'

cookie = {'visit-month': 'April'}
#Adding default cookie
se=requests.session()
se.cookies.update(cookie)

response = se.get(url=url, allow_redirects=False, timeout=1, cookies={'visit-year': '2022'})
print(response.history)
print(response.status_code)
print(response.content)
