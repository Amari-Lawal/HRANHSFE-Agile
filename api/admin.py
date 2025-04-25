from fastapi import APIRouter
from api.HRAModels import Vendor,MedicineAsset,User

from api.db_session import hracrud
from api.db_session import hranhsjwt
from fastapi import Header
from typing import Optional

router = APIRouter(prefix="/api/v1/admin", tags=["admin"])

@router.delete("/delete_all_data_from_tables")
async def delete_all_data_from_tables(authorization: str = Header(None)):
    try:
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            authorized = hranhsjwt.authenticate_user(authorization)
            if authorized.role == "admin":
                hracrud.delete_all_data_from_tables(User.USERSTABLENAME)
                hracrud.delete_all_data_from_tables(Vendor.VENDORTABLENAME)
                hracrud.delete_all_data_from_tables(MedicineAsset.MEDICINEASSETSTABLENAME)
                return {"message":"All data was deleted."}
            else:
                return {"error":"User is not authorized."}

        else:
            return {"error":"User does not exist or is not authorized."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}