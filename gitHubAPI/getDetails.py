import requests
from utilities.configurations import getConfig , getToken
from utilities.resources import GITResource

se = requests.session()
se.headers = getToken()


url = getConfig()['GITAPI']['endpoint'] + GITResource.getDetails
response = se.get(url)

print(response.content)