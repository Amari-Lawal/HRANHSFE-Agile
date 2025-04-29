import uvicorn

from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from api import assets, users, vendors,admin
from pages import assetspage, home,auth
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
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
app.include_router(admin.router)
app.include_router(assetspage.router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Check for our specific error type
    #print(exc.errors())
    for error in exc.errors():
        return JSONResponse(
            status_code=422,
            content={"error": error['msg']},
        )

    # Default fallback
    return JSONResponse(
        status_code=422,
        content={"error": "Exception Error"},
    )
if __name__ == "__main__":
    uvicorn.run("main:app",port=8080,log_level="info")
