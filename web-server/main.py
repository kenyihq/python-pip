import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return '''
        <h1>Soy un H1</h1>
        <h2>Soy un H2</h2>
        <h3>Soy un H3</h3>
        <h4>Soy un H4</h4>
    '''

def run():
    store.get_categories()


if __name__ == '__main__':
    run()