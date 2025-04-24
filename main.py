import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import assets, users, vendors
from pages import home,auth
from fastapi.staticfiles import StaticFiles
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



app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(users.router)
app.include_router(vendors.router)
app.include_router(assets.router)
app.include_router(home.router)  # Include HTML page routes
app.include_router(auth.router)
if __name__ == "__main__":
    uvicorn.run("main:app",port=8080,log_level="info")
