import requests



def get_categories():
    URL = 'https://api.escuelajs.co/api/v1/categories'
    res = requests.get(URL)
    print(res.status_code)
    print(res.text)
