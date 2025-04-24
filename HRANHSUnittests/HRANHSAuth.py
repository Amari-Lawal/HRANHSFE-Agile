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
    def test_create_MedicineAsset(self):
        self.test_signup()
        response = requests.post(f"{uri}/api/v1/login",json={"email":HRANHSAuth.EMAIL,"password":HRANHSAuth.PASSWORD})
        access_token = response.json()["access_token"]
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.post(f"{uri}/api/v1/create_asset",headers=headers,json={
                "drug_name": "Aspirin",
                "description": "Pain reliever and anti-inflammatory",
                "category": "Pain Relief",
                "lot_number": "AB12345",
                "manufacture_date": "2023-05-10",
                "purchase_cost": 12.99,
                "vendor": "Pharma Inc.",
                "storage_location": "Shelf A1",
                "status": "Active",
                "expiration_date": "2025-05-10",
                "last_reviewed": "2024-04-15",
                "next_review": "2025-04-15",
                "storage_conditions": "Cool and dry place",
                "useful_life_years": 2,
                "current_stock": 100,
                "image_url": "https://example.com/images/aspirin.jpg"
                }
                )






if __name__ == "__main__":
    unittest.main()