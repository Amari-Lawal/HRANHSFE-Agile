import requests
from HRANHSUnittests.HRANHSConstantsTests import HRANHSConstantsTests
import unittest
class HRANHSignupTest:
    @staticmethod
    def signup(self: unittest.TestCase):
        response = requests.post(f"{HRANHSConstantsTests.URI}/api/v1/users/signup",json={
            "first_name": "Alice",
            "last_name": "Johnson",
            "email": HRANHSConstantsTests.EMAIL,
            "password": HRANHSConstantsTests.PASSWORD,
            "role": "admin",
            "department": "Engineering",
            "phone_number": "+1234567890",
            "status": "active",
            "last_login": "2025-04-23T12:34:56",
            "created_at": "2024-12-01T09:15:30",
            "updated_at": "2025-04-22T17:45:10"
            })
        self.assertEqual(response.json().get("error"),None)
        self.assertNotEqual(response.json().get("error"),"you have already done this action can't gain tokens.")

        return response