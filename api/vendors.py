from fastapi import APIRouter
from api.HRAModels import Vendor
from api.db_session import hracrud
from api.db_session import hranhsjwt
from fastapi import Header
from typing import Optional

router = APIRouter(prefix="/api/v1/vendors", tags=["vendors"])

@router.post("/create_vendor")
async def create_vendor(vendor:Vendor,authorization: str = Header(None)):
    try:
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            condition = f"{Vendor.get_field_name("vendor_name")} = '{vendor.vendor_name}'"
            vendor_exists = hracrud.check_exists(("*"),Vendor.VENDORTABLENAME,condition=condition)
            if vendor_exists:
                return {"message": "Vendor already exists"} # , 400
            elif not vendor_exists:
                hracrud.post_data(Vendor.fields_to_tuple(),vendor.values_to_tuple(),table=Vendor.VENDORTABLENAME)
                return {"message":"Vendor was created."}
            
        else:
            return {"error":"User does not exist or is not authorized."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
@router.get("/get_all_vendors")
async def get_all_vendors(authorization: str = Header(None)):
    try:
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            asset_exists = hracrud.check_exists(("*"),Vendor.VENDORTABLENAME)
            if asset_exists:
                results = hracrud.get_data(Vendor.fields_to_tuple(),Vendor.VENDORTABLENAME)
                return {"vendors":results}
            else:
                return {"message":"No vendors found."} 
        else:
            return {"error":"User does not exist or is not authorized."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
@router.get("/get_vendor/{vendor_id}")
async def get_vendor(vendor_id:Optional[str] = None,vendor_name:Optional[str] = None,authorization: str = Header(None)):
    try:
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            if vendor_id:   
                condition = f"{Vendor.get_field_name('vendor_id')} = '{vendor_id}'" 
            elif vendor_name:
                condition = f"{Vendor.get_field_name('vendor_name')} = '{vendor_name}'"
            else:
                return {"error":"Please provide vendor_id or vendor_name."}
            vendor_exists = hracrud.check_exists(("*"),Vendor.VENDORTABLENAME,condition=condition)
            if vendor_exists:
                results = hracrud.get_data(Vendor.fields_to_tuple(),Vendor.VENDORTABLENAME,condition=condition)
                return {"vendors":results}
            else:
                return {"message":"No assets found."} 
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
                return {"message":"Medicine Asset was deleted."}
            else:
                return {"error":"No assets found."} 
        else:
            return {"error":"User does not exist or is not authorized."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}