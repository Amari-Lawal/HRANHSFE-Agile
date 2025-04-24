import requests
from HRANHSUnittests.HRANHSConstantsTests import HRANHSConstantsTests
class HRANHSRolesTest:
    @staticmethod
    def get_user_role(headers):
        response = requests.get(f"{HRANHSConstantsTests.URI}/api/v1/users/get_user_role", headers=headers)
        return response.json()