import requests
from HRANHSUnittests.HRANHSConstantsTests import HRANHSConstantsTests
class HRANHSLoginTest:
    @staticmethod
    def login():
        response = requests.post(f"{HRANHSConstantsTests.URI}/api/v1/users/login",json={"email":HRANHSConstantsTests.EMAIL,"password":HRANHSConstantsTests.PASSWORD})
        access_token = response.json()["access_token"]
        headers = {"Authorization": f"Bearer {access_token}"}
        return headers