import requests
from behave import *

from payload.postPayload import addCollectionPayload
from utilities.configurations import getConfig, getHeaders, getToken
from utilities.resources import APIResource
from utilities.resources import GITResource


@given('the Collection details which needs to be added')
def step_implementation(context):
    context.url = getConfig()['API']['endpoint'] + APIResource.createCollection
    context.payload = addCollectionPayload("Sample 123")


@when('we execute Add Collection PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=getHeaders())


@then('the collection should be successfully added')
def step_impl(context):
    print(context.response.status_code)
    response_json = context.response.json()
    print(response_json['collection']['uid'])
    context.uid = response_json['collection']['uid']


@given('the Collection details which {name} to be added')
def step_implementation(context, name):
    context.url = getConfig()['API']['endpoint'] + APIResource.createCollection
    context.payload = addCollectionPayload(name)


# GitHub Steps

@given('I have github credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.headers = getToken()


@when('I hit get repo API of Github')
def step_impl(context):
    context.url = getConfig()['GITAPI']['endpoint'] + GITResource.getRepos
    context.response = context.se.get(context.url)


@then('Status Code of Response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode
