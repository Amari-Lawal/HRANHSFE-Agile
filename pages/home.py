# pages/home.py
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter() # APIRouter(prefix="/pages", tags=["pages"])

@router.get("/")
async def render_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
