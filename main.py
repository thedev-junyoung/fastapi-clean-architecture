from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"hello": "FastAPI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)