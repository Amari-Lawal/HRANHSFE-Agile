
from fastapi import APIRouter
from api.db_session import hracrud
from api.db_session import hranhsjwt
from fastapi import Header
from api.HRAModels import MedicineAsset
from api.HRANHSConstants import HRANHSConstants
router = APIRouter(prefix="/api/v1/assets", tags=["assets"])

@router.post("/create_medicine_asset")
async def create_medicine_asset(asset:MedicineAsset,authorization: str = Header(None)):
    try:
        user_auth_role = hranhsjwt.secure_decode(authorization.replace("Bearer ",""))
        current_user = user_auth_role["email"]
        role = user_auth_role["role"]
        if current_user:
            if role == HRANHSConstants.ADMIN:
                condition = f"{MedicineAsset.get_field_name("medicine_asset")} = '{asset.medicine_asset}'"
                asset_exists = hracrud.check_exists(("*"),MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
                if asset_exists:
                    return {"message": "Medicine Asset already exists"} # , 400
                elif not asset_exists:
                    hracrud.post_data(MedicineAsset.fields_to_tuple(),asset.values_to_tuple(),table=MedicineAsset.MEDICINEASSETSTABLENAME)
                    return {"message":"Medicine Asset was created."}
            else:
                return {"error":"Incorrect permissions."}
           
            
        else:
            return {"error":"User does not exist."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
@router.get("/get_all_medicine_assets")
async def get_all_medicine_assets(authorization: str = Header(None)):
    try:
        user_auth_role = hranhsjwt.secure_decode(authorization.replace("Bearer ",""))
        current_user = user_auth_role["email"]
        role = user_auth_role["role"]
        if current_user:
            asset_exists = hracrud.check_exists(("*"),MedicineAsset.MEDICINEASSETSTABLENAME)
            if asset_exists:
                results = hracrud.get_data(MedicineAsset.fields_to_tuple(),MedicineAsset.MEDICINEASSETSTABLENAME)
                return {"medicine_assets":results}
            else:
                return {"message":"No assets found."} 
        else:
            return {"error":"User does not exist."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
@router.get("/get_medicine_asset")
async def get_medicine_asset(medicine_asset:str,authorization: str = Header(None)):
    try:
        user_auth_role = hranhsjwt.secure_decode(authorization.replace("Bearer ",""))
        current_user = user_auth_role["email"]
        role = user_auth_role["role"]
        if current_user:
            condition = f"{MedicineAsset.get_field_name('medicine_asset')} = '{medicine_asset}'"
            asset_exists = hracrud.check_exists(("*"),MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
            if asset_exists:
                results = hracrud.get_data(MedicineAsset.fields_to_tuple(),MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
                return {"medicine_assets":results}
            else:
                return {"message":"No assets found."} 
        else:
            return {"error":"User does not exist."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}