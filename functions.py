import requests
def getquote():
    url = 'https://api.chucknorris.io/jokes/random'
    try:
        response = requests.get(url).text
        return response
    except:
        return '{"value":"Error could not get quote"}';