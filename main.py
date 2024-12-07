from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def hello_world():
    return {'hello':'world'}


@app.get("/squared/{n}")
def squared(n: int, q: str = None):
    return {'squared':n*n, 'context':q}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:handler", host="0.0.0.0", port=5000, workers=1)