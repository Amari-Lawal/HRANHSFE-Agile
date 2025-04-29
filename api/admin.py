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
            admin_only = hranhsjwt.restrict_access(authorization)
            if admin_only:
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
async def delete_vendor(vendor_id:str,authorization: str = Header(None)):
    try:
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            admin_only = hranhsjwt.restrict_access(authorization)
            if admin_only:
                condition = f"{Vendor.get_field_name('vendor_id')} = '{vendor_id}'" 
                asset_exists = hracrud.check_exists(("*"),Vendor.VENDORTABLENAME,condition=condition)
                if asset_exists:
                    hracrud.delete_data(Vendor.VENDORTABLENAME,condition=condition)
                    hracrud.delete_data(MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
                    return {"message":"Vendor was deleted."}
                else:
                    return {"error":"No assets found."} 
            else:
                return {"error":"User is not authorized."}
        else:
            return {"error":"User does not exist or is not authorized."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
@router.delete("/delete_medicine_asset/{medicine_id}")
async def delete_medicine_asset(medicine_id:str,authorization: str = Header(None)):
    try:
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            admin_only = hranhsjwt.restrict_access(authorization)
            if admin_only:
                condition = f"{MedicineAsset.get_field_name('medicine_id')} = '{medicine_id}'" 
                asset_exists = hracrud.check_exists(("*"),MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
                if asset_exists:
                    hracrud.delete_data(MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
                    return {"message":"Medicine Asset was deleted."}
                else:
                    return {"error":"No assets found."} 
            else:
                return {"error":"User is not authorized."}
        else:
            return {"error":"User does not exist or is not authorized."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
@router.delete("/delete_user/{email}")
async def delete_user(email:str,authorization: str = Header(None)):
    try:
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            admin_only = hranhsjwt.restrict_access(authorization)
            if admin_only:
                condition = f"{User.get_field_name('email')} = '{email}'" 
                user_exists = hracrud.check_exists(("*"),User.USERSTABLENAME,condition=condition)
                if user_exists:
                    hracrud.delete_data(User.USERSTABLENAME,condition=condition)
                    return {"message":"User was deleted."}
                else:
                    return {"error":"No assets found."} 
            else:
                return {"error":"User is not authorized."}
        else:
            return {"error":"User does not exist or is not authorized."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}