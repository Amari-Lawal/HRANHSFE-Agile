# pages/home.py
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/login")
async def render_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
@router.get("/signup")
async def render_login(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})
