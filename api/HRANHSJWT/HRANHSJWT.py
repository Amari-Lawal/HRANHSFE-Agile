import jwt
import hashlib
from api.HRANHSDB import HRANHSCRUD
from api.HRANHSJWT import HRANHSJWT
from api.HRAModels import User
from fastapi import Header
from api.HRANHSConstants import HRANHSConstants
from api.HRANHSJWT.models.UserAuthRole import UserAuthRole
class HRANHSJWT:
    def __init__(self,hracrud : HRANHSCRUD) -> None:
        self.hracrud = hracrud
        self.JWT_SECRET = HRANHSConstants.JWT_SECRET_KEY  #'super-secret'
        # IRL we should NEVER hardcode the secret: it should be an evironment variable!!!
        self.JWT_ALGORITHM = "HS256"
    def secure_encode(self,token):
        # if we want to sign/encrypt the JSON object: {"hello": "world"}, we can do it as follows
        # encoded = jwt.encode({"hello": "world"}, self.JWT_SECRET, algorithm=self.JWT_ALGORITHM)
        encoded_token = jwt.encode(token, self.JWT_SECRET, algorithm=self.JWT_ALGORITHM)
        # this is often used on the client side to encode the user's email address or other properties
        return encoded_token

    def secure_decode(self,token):
        # if we want to sign/encrypt the JSON object: {"hello": "world"}, we can do it as follows
        # encoded = jwt.encode({"hello": "world"}, self.JWT_SECRET, algorithm=self.JWT_ALGORITHM)
        decoded_token = jwt.decode(token, self.JWT_SECRET, algorithms=self.JWT_ALGORITHM)
        # this is often used on the client side to encode the user's email address or other properties
        return decoded_token
    def provide_access_token(self,user: User):
        condition = f"email = '{user.email}'"
        email_exists = self.hracrud.check_exists(("*"),User.USERSTABLENAME,condition=condition)
        if email_exists:
            encrypted_password =  hashlib.sha256(user.password.encode('utf-8')).hexdigest()
            email_data = self.hracrud.get_data(User.fields_to_tuple(),User.USERSTABLENAME,condition=condition)[0]
            if email_data["password"] == encrypted_password:
                access_token = self.secure_encode({"email":email_data["email"],"role":email_data["role"]}) #create_access_token(identity=email_exists["email"])
                return access_token
            else:
                return "Wrong password"
        else:
            return "Wrong password"
    def authenticate_user(self,authorization: str = Header(None)) ->UserAuthRole:
        token = authorization.replace("Bearer ","")
        user_auth_role = self.secure_decode(token)
        return UserAuthRole.model_validate(user_auth_role)
    def check_user_role(self,authorization: str = Header(None)) -> bool:
        user_auth_role = self.authenticate_user(authorization)
        user_role = user_auth_role.role
        current_user = user_auth_role.email
        user_role_exists = self.hracrud.check_exists(("*"),User.USERSTABLENAME,condition=f"{User.get_field_name('email')} = '{current_user}' AND {User.get_field_name('role')} = '{user_role}'")
        if user_role_exists:
            return True
        else:
            return False
    def check_user_exists(self,authorization: str = Header(None)) -> bool:
        user_auth_role = self.authenticate_user(authorization)
        current_user = user_auth_role.email
        user_exists = self.hracrud.check_exists(("*"),User.USERSTABLENAME,condition=f"{User.get_field_name('email')} = '{current_user}'")
        if user_exists:
            return True
        else:
            return False
    def restrict_access(self,authorization: str = Header(None)) -> bool:
        user_auth_role = self.authenticate_user(authorization)
        current_user = user_auth_role.email
        user_role = user_auth_role.role
        user_role_exists = self.hracrud.check_exists(("*"),User.USERSTABLENAME,condition=f"{User.get_field_name('email')} = '{current_user}' AND {User.get_field_name('role')} = '{user_role}'")
        if user_role_exists:
            result = self.hracrud.get_data(User.fields_to_tuple(),User.USERSTABLENAME,condition=f"{User.get_field_name('email')} = '{current_user}'")
            user_data = self.hracrud.get_first_data_point(result)
            user_model = User(**user_data)
            if user_model.role == HRANHSConstants.ADMIN:
                return True
            else:
                return False
        else:
            return False