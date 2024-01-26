import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/home")
async def home():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
