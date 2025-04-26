import requests
import unittest
from api.HRAModels import User   
from api.HRAResponses import UserResponse
from api.HRARequests.UpdateUser import UpdateUser
from HRANHSUnittests.HRANHSTestCases import HRANHSTestCases
from HRANHSUnittests.HRANHSConstantsTests import HRANHSConstantsTests
from api.HRAResponses import UserResponse
class HRANHSAuthTest:
    @staticmethod
    def login():
        response = requests.post(f"{HRANHSConstantsTests.PUBLIC_URI}/api/v1/users/login",json={"email":HRANHSConstantsTests.EMAIL,"password":HRANHSConstantsTests.PASSWORD})
        access_token = response.json()["access_token"]
        headers = {"Authorization": f"Bearer {access_token}"}
        return headers
    @staticmethod
    def signup(self: unittest.TestCase):
        response = requests.post(f"{HRANHSConstantsTests.PUBLIC_URI}/api/v1/users/signup",json=HRANHSTestCases.USER_SIGNUP_ADMIN_TEST_CASE)
        self.assertEqual(response.json().get("error"),None)
        self.assertNotEqual(response.json().get("error"),"you have already done this action can't gain tokens.")

        return response
    @staticmethod
    def get_user_data(headers) -> User:
        response = requests.get(f"{HRANHSConstantsTests.PUBLIC_URI}/api/v1/users/get_user_data", headers=headers)
        return User(**response.json())
    @staticmethod
    def get_all_user_data(headers) -> User:
        response = requests.get(f"{HRANHSConstantsTests.PUBLIC_URI}/api/v1/users/get_all_user_data", headers=headers)
        user_response = response.json()
        if "users" in user_response:
            return  UserResponse(**user_response)
        else:
            return user_response
    @staticmethod
    def update_user(headers:dict,user_id:str,user_data : UpdateUser):
        response = requests.put(f"{HRANHSConstantsTests.PUBLIC_URI}/api/v1/users/update_user/{user_id}",headers=headers,json=user_data)
        return response.json()
    @staticmethod
    def delete_user(headers:dict,user_id:str):
        response = requests.delete(f"{HRANHSConstantsTests.PUBLIC_URI}/api/v1/admin/delete_user/{user_id}",headers=headers)
        return response.json()
    @staticmethod
    def get_first_user_id(users:UserResponse) -> str:
        if users:
            return users.users[0].user_id
        else:
            return None