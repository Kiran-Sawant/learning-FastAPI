from fastapi import FastAPI

# creating FastApi instance.
app = FastAPI()

# @api_instance.http_method("URL path")
@app.get('/')
def index():
    return {"data": {'name': 'Kiran'}}

@app.get('/about')
def about():
    return {"data": {'about': 'About page'}}