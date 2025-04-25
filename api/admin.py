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
@router.delete("/delete_vendor/{vendor_id}")
async def delete_vendor(vendor_id:Optional[str] = None,authorization: str = Header(None)):
    try:
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            if vendor_id:   
                condition = f"{Vendor.get_field_name('vendor_id')} = '{vendor_id}'" 
            else:
                return {"error":"Please provide vendor_id or vendor."}
            asset_exists = hracrud.check_exists(("*"),Vendor.VENDORTABLENAME,condition=condition)
            if asset_exists:
                hracrud.delete_data(Vendor.VENDORTABLENAME,condition=condition)
                hracrud.delete_data(MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
                return {"message":"Vendor was deleted."}
            else:
                return {"error":"No assets found."} 
        else:
            return {"error":"User does not exist or is not authorized."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
@router.delete("/delete_medicine_asset/{medicine_id}")
async def delete_medicine_asset(medicine_id:Optional[str] = None,authorization: str = Header(None)):
    try:
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            if medicine_id:   
                condition = f"{MedicineAsset.get_field_name('medicine_id')} = '{medicine_id}'" 
            else:
                return {"error":"Please provide medicine_id or medicine_asset."}
            asset_exists = hracrud.check_exists(("*"),MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
            if asset_exists:
                hracrud.delete_data(MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
                return {"message":"Medicine Asset was deleted."}
            else:
                return {"error":"No assets found."} 
        else:
            return {"error":"User does not exist or is not authorized."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}