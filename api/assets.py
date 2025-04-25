
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
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            condition = f"{MedicineAsset.get_field_name("medicine_asset")} = '{asset.medicine_asset}'"
            asset_exists = hracrud.check_exists(("*"),MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
            if asset_exists:
                return {"message": "Medicine Asset already exists"} # , 400
            elif not asset_exists:
                hracrud.post_data(MedicineAsset.fields_to_tuple(),asset.values_to_tuple(),table=MedicineAsset.MEDICINEASSETSTABLENAME)
                return {"message":"Medicine Asset was created."}
        else:
            return {"error":"User does not exist or is not authorized."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
@router.get("/get_all_medicine_assets")
async def get_all_medicine_assets(authorization: str = Header(None)):
    try:
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            asset_exists = hracrud.check_exists(("*"),MedicineAsset.MEDICINEASSETSTABLENAME)
            if asset_exists:
                results = hracrud.get_data(MedicineAsset.fields_to_tuple(),MedicineAsset.MEDICINEASSETSTABLENAME)
                return {"medicine_assets":results}
            else:
                return {"error":"No assets found."} 
        else:
            return {"error":"User does not exist or is not authorized."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
@router.get("/get_medicine_asset")
async def get_medicine_asset(medicine_id:Optional[str] = None,medicine_asset:Optional[str] = None,authorization: str = Header(None)):
    try:
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            if medicine_id:   
                condition = f"{MedicineAsset.get_field_name('medicine_id')} = '{medicine_id}'" 
            elif medicine_asset:
                condition = f"{MedicineAsset.get_field_name('medicine_asset')} = '{medicine_asset}'"
            else:
                return {"error":"Please provide medicine_id or medicine_asset."}
            asset_exists = hracrud.check_exists(("*"),MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
            if asset_exists:
                results = hracrud.get_data(MedicineAsset.fields_to_tuple(),MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
                return {"medicine_assets":results}
            else:
                return {"error":"No assets found."} 
        else:
            return {"error":"User does not exist or is not authorized."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
@router.get("/get_medicine_assets_by_vendor/{vendor_id}")
async def get_medicine_assets_by_vendor(vendor_id:str,authorization: str = Header(None)):
    try:
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            condition = f"{MedicineAsset.get_field_name('vendor_id')} = '{vendor_id}'"
            asset_exists = hracrud.check_exists(("*"),MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
            if asset_exists:
                results = hracrud.get_data(MedicineAsset.fields_to_tuple(),MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
                return {"medicine_assets":results}
            else:
                return {"error":"No assets found."} 
        else:
            return {"error":"User does not exist or is not authorized."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
@router.put("/update_medicine_asset/{medicine_id}")
async def update_medicine_asset(medicine_id:str,asset:HRAUpdateMedicineAsset,authorization: str = Header(None)):
    try:
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            print(medicine_id)
            condition = f"{MedicineAsset.get_field_name('medicine_id')} = '{medicine_id}'"
            asset_exists = hracrud.check_exists(("*"),MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
            if asset_exists:
                hracrud.update_data(asset.fields_from_existing_to_tuple(),asset.values_from_existing_to_tuple(),table=MedicineAsset.MEDICINEASSETSTABLENAME,condition=condition)
                return {"mesage":"Medicine Asset was updated."}
            else:
                return {"error":"No asset found."} 
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