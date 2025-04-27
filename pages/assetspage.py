# pages/home.py
from fastapi import APIRouter, Request,Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
from api.db_session import hracrud
from api.HRAModels import MedicineAsset,Vendor
templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/assets", tags=["assets"])




@router.get("")
async def render_assets(request: Request):
    assets = hracrud.get_data(MedicineAsset.fields_to_tuple(),MedicineAsset.MEDICINEASSETSTABLENAME)
    vendors = hracrud.get_data(Vendor.fields_to_tuple(),Vendor.VENDORTABLENAME)
    return templates.TemplateResponse("assets.html", {"request": request,"assets": assets,"vendors":vendors},status_code=200)
