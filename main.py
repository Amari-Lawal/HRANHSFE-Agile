import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import assets, users, vendors

app = FastAPI()


from datetime import datetime
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






@app.get('/')# GET # allow all origins all methods.
async def index():
    return "Welcome to HRANHS Template. Hello"
app.include_router(users.router)
app.include_router(vendors.router)
app.include_router(assets.router)

if __name__ == "__main__":
    uvicorn.run("main:app",port=8080,log_level="info")
