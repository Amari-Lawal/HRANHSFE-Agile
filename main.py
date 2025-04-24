import uvicorn
import hashlib
from fastapi import FastAPI, Header,Request,File, UploadFile,status,Form
from fastapi.responses import StreamingResponse,FileResponse,Response
from typing import Dict,List,Any,Union
from HRANHSDB.HRANHSCRUD import HRANHSCRUD
from HRANHSDB.HRANHSHash import HRANHSHash
from fastapi.middleware.cors import CORSMiddleware
from HRANHSJWT import HRANHSJWT
from HRANHSDB import HRANHSCreateTables 
from HRAModels import User,UserLogin,MedicineAsset
from HRANHSConstants import HRANHSConstants
from datetime import datetime
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


hracrud = HRANHSCRUD()
hranhsjwt = HRANHSJWT(hracrud)
HRANHSCreateTables.create(hracrud)


@app.get('/')# GET # allow all origins all methods.
async def index():
    return "Welcome to HRANHS Template. Hello"
@app.post('/api/v1/signup') # POST
async def signup(user: User):
    try:
        user.password = hashlib.sha256(user.password.encode('utf-8')).hexdigest()
        condition = f"email = '{user.email}'"
        email_exists = hracrud.check_exists(("*"),User.USERSTABLENAME,condition=condition)
        if email_exists:
            return {"message": "Email already exists"} # , 400
        elif not email_exists:
            hracrud.post_data(User.fields_to_tuple(),user.values_to_tuple(),table=User.USERSTABLENAME)
            access_token = hranhsjwt.secure_encode({"email":user.email,"role":user.role})
            callback = {"status": "success","access_token":access_token}

            return callback
    except Exception as ex:
        error_detected = {"error": "error occured","errortype":type(ex), "error": str(ex)}
        return error_detected
@app.post('/api/v1/login') # POST
async def login(user :UserLogin): # ,authorization: str = Header(None)
    # Login API
    try:
        condition = f"email = '{user.email}'"
        email_exists = hracrud.check_exists(("*"),User.USERSTABLENAME,condition=condition)
        if email_exists:
            access_token = hranhsjwt.provide_access_token(user)
            if access_token == "Wrong password":
                return {"message": "The username or password is incorrect."}
            else:
                last_login = User.get_field_name("last_login")
                now = datetime.now().strftime(HRANHSConstants.DATEFORMAT)
                hracrud.update_data((last_login,),(now,),User.USERSTABLENAME,condition=condition)
                return {"access_token": access_token}
        return {"message": "The username or password is incorrect."}
    except Exception as ex:
        return {"error": f"{type(ex)} {str(ex)}"}

@app.get('/api/v1/get_user_role') # POST # allow all origins all methods.
async def get_user_role(authorization: str = Header(None)):
    try:
        user_auth_role = hranhsjwt.secure_decode(authorization.replace("Bearer ",""))
        current_user = user_auth_role["email"]
        role = user_auth_role["role"]
        if current_user:
            return {"email":current_user,"role":role}
            
        else:
            return {"error":"User does not exist."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
@app.post("/api/v1/create_medicine_asset")
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
@app.get("/api/v1/get_all_medicine_assets")
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
@app.get("/api/v1/get_medicine_asset")
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
if __name__ == "__main__":
    uvicorn.run("main:app",port=8080,log_level="info")
