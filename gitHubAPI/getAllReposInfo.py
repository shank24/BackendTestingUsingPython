import requests
from utilities.configurations import getConfig, getToken
from utilities.resources import GITResource

#This session has required authentication stored in the se.
se = requests.session()
se.headers = getToken()

url = getConfig()['GITAPI']['endpoint'] + GITResource.getRepos
response = se.get(url)

print(response.status_code)