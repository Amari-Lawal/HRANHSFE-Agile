from fastapi import APIRouter
from api.db_session import hracrud
from api.db_session import hranhsjwt
from fastapi import Header
from api.HRAModels import User,UserLogin
from datetime import datetime
import hashlib   
from api.HRANHSConstants import HRANHSConstants
from api.HRARequests.UpdateUser import UpdateUser
router = APIRouter(prefix="/api/v1/users", tags=["users"])

@router.post('/signup') # POST
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
@router.post('/login') # POST
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

@router.get('/get_all_user_data') # POST # allow all origins all methods.
async def get_all_user_data(authorization: str = Header(None)):
    try:
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            results = hracrud.get_data(User.fields_to_tuple(),User.USERSTABLENAME)
            return {"users":results}            
        else:
            return {"error":"User does not exist or is not authorized."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
@router.get('/decode_user') # POST # allow all origins all methods.
async def decode_user(authorization: str = Header(None)):
    try:
        decoded_user = hranhsjwt.authenticate_user(authorization)
        return decoded_user

    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
@router.get('/get_user_data') # POST # allow all origins all methods.
async def get_user_data(authorization: str = Header(None)):
    try:
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            user_auth_role = hranhsjwt.authenticate_user(authorization)
            current_user = user_auth_role.email
      
            condition = f"{User.get_field_name('email')} = '{current_user}'"
            user_exists = hracrud.check_exists(("*"),User.USERSTABLENAME,condition=condition)
            if user_exists:
                results = hracrud.get_data(User.fields_to_tuple(),User.USERSTABLENAME,condition=condition)
                result = hracrud.get_first_data_point(results)
                return result
            else:
                return {"error":"No user found."}
            
        else:
            return {"error":"User does not exist or is not authorized."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}

@router.put("/update_user/{email}")
async def update_user(email:str,user:UpdateUser,authorization: str = Header(None)):
    try:
        authenticated = hranhsjwt.check_user_role(authorization)
        if authenticated:
            condition = f"{User.get_field_name('email')} = '{email}'"
            user_exists = hracrud.check_exists(("*"),User.USERSTABLENAME,condition=condition)
            if user_exists:
                hracrud.update_data(user.fields_from_existing_to_tuple(),user.values_from_existing_to_tuple(),table=User.USERSTABLENAME,condition=condition)
                return {"mesage":"User was updated."}
            else:
                return {"error":"No asset found."} 
        else:
            return {"error":"User does not exist or is not authorized."}
    except Exception as ex:
        print(type(ex),ex)
        return {"error":f"{type(ex)},{ex}"}
