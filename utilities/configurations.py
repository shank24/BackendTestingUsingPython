import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('/home/shanky/PycharmProjects/backendTesting/utilities/properties.ini')
    return config


def getHeaders():
    headers = {"X-Api-Key": "PMAK-5fbc920d2e116d00438ba11a-0fbc28fc41915c6b7c533c28a9ec5132fd",
               "Content-Type": "application/json"}
    return headers


def getToken():
    headers = {"authorization": "Bearer f4b97769c3b0736020dbc92b46a7412f279aaf65",
               "Content-Type": "application/json"}
    return headers
