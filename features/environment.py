import requests
from utilities.configurations import getHeaders


def after_scenario(context, scenario):
    delete_response = requests.delete(context.url + "/" + context.uid, headers=getHeaders())
    print(delete_response.status_code)
