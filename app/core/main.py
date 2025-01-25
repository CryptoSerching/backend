from fastapi import FastAPI
import uvicorn

if "__main__" == __name__:
    app = FastAPI()
    uvicorn.run(app, host="8000")