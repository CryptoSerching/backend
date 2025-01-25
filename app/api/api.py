from fastapi import FastAPI

app = FastAPI()
@app.route()
def index():
    return {"message": "Hello World"}