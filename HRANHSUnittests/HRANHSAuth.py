import json
import requests
import unittest
import sys

uri = "http://127.0.0.1:8080" #"https://blacktechdivisionreward-hrjw5cc7pa-uc.a.run.app"

class HRANHSAuth(unittest.TestCase):
    EMAIL = "alice.johnson@example.com"
    PASSWORD = "hello" 
    def signup(self):
        response = requests.post(f"{uri}/api/v1/signup",json={
        "first_name": "Alice",
        "last_name": "Johnson",
        "email": HRANHSAuth.EMAIL,
        "password": HRANHSAuth.PASSWORD,
        "role": "admin",
        "department": "Engineering",
        "phone_number": "+1234567890",
        "status": "active",
        "last_login": "2025-04-23T12:34:56",
        "created_at": "2024-12-01T09:15:30",
        "updated_at": "2025-04-22T17:45:10"
        })
        print(response.json())
        self.assertEqual(response.json().get("error"),None)
        self.assertNotEqual(response.json().get("error"),"you have already done this action can't gain tokens.")


    def test_signup(self):
        self.signup()
    def test_login(self):
        self.test_signup()
        response = requests.post(f"{uri}/api/v1/login",json={"email":HRANHSAuth.EMAIL,"password":HRANHSAuth.PASSWORD})
        print(response.json())
    def test_get_user_role(self):
        self.signup()
        response = requests.post(f"{uri}/api/v1/login",json={"email":HRANHSAuth.EMAIL,"password":HRANHSAuth.PASSWORD})
        access_token = response.json()["access_token"]
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(f"{uri}/api/v1/get_user_role",headers=headers)
        print(response.json())
    def test_create_asset():
        pass






if __name__ == "__main__":
    unittest.main()