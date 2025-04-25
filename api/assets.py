
from fastapi import APIRouter
from api.db_session import hracrud
from api.db_session import hranhsjwt
from fastapi import Header
from api.HRAModels import MedicineAsset
from api.HRARequests import HRAUpdateMedicineAsset
from api.HRANHSConstants import HRANHSConstants
from typing import Optional
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
                return {"error":"No assets found."} 
        else:
            return {"error":"User does not exist."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
@router.get("/get_medicine_asset")
async def get_medicine_asset(medicine_id:Optional[str] = None,medicine_asset:Optional[str] = None,authorization: str = Header(None)):
    try:
        user_auth_role = hranhsjwt.secure_decode(authorization.replace("Bearer ",""))
        current_user = user_auth_role["email"]
        role = user_auth_role["role"]
        if current_user:
            if medicine_id:   
                condition = f"{MedicineAsset.get_field_name('medicine_id')} = '{medicine_id}'" 
            elif medicine_asset:
                condition = f"{MedicineAsset.get_field_name('medicine_asset')} = '{medicine_asset}'"
            else:
                return {"error":"Please provide medicine_id or medicine_asset."}
            asset_exists = hracrud.check_exists(("*"),MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
            print(asset_exists)
            if asset_exists:
                results = hracrud.get_data(MedicineAsset.fields_to_tuple(),MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
                return {"medicine_assets":results}
            else:
                return {"error":"No assets found."} 
        else:
            return {"error":"User does not exist."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
@router.put("/update_medicine_asset/{medicine_id}")
async def update_medicine_asset(medicine_id:str,asset:HRAUpdateMedicineAsset,authorization: str = Header(None)):
    try:
        user_auth_role = hranhsjwt.secure_decode(authorization.replace("Bearer ",""))
        current_user = user_auth_role["email"]
        role = user_auth_role["role"]
        if current_user:
            print(medicine_id)
            condition = f"{MedicineAsset.get_field_name('medicine_id')} = '{medicine_id}'"
            asset_exists = hracrud.check_exists(("*"),MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
            if asset_exists:
                hracrud.update_data(asset.fields_from_existing_to_tuple(),asset.values_from_existing_to_tuple(),table=MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
                return {"mesage":"Medicine Asset was updated."}
            else:
                return {"error":"No asset found."} 
        else:
            return {"error":"User does not exist."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}