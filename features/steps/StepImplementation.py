import requests
from behave import *

from payload.postPayload import addCollectionPayload
from utilities.configurations import getConfig, getHeaders
from utilities.resources import APIResource


@given('the Collection details which needs to be added')
def step_implementation(context):
    context.url = getConfig()['API']['endpoint'] + APIResource.createCollection
    context.payload = addCollectionPayload()


@when('we execute Add Collection PostAPI method')
def step_impl(context):
    context.post_response = requests.post(context.url, json=context.payload, headers=getHeaders())


@then('the collection should be successfully added')
def step_impl(context):
    print(context.post_response.status_code)
    response_json = context.post_response.json()
    print(response_json['collection']['uid'])
    context.uid = response_json['collection']['uid']
