# pages/home.py
from fastapi import APIRouter, Request,Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.templating import Jinja2Templates
from api.db_session import hranhsjwt,hracrud
from api.HRAModels import MedicineAsset
templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/assets", tags=["assets"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):

    if hranhsjwt.check_user_role(token):
        user_auth_role = hranhsjwt.authenticate_user(token)
        return user_auth_role.model_dump()
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.get("")
async def render_assets(request: Request,current_user: dict = Depends(get_current_user)):
    assets = hracrud.get_data(MedicineAsset.fields_to_tuple(),MedicineAsset.MEDICINEASSETSTABLENAME)
    return templates.TemplateResponse("assets.html", {"request": request,"current_user": current_user,"assets": assets},status_code=200)
