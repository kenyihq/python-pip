import requests



def get_categories():
    URL = 'https://api.escuelajs.co/api/v1/categories'
    res = requests.get(URL)
    print(res.status_code)
    print(res.text)

    categories = res.json()

    for category in categories:
        name = category["name"]
        img = category["image"]
        print(f"{name} : {img}")
