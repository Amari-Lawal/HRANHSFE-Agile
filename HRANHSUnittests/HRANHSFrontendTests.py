import requests
from typing import Optional
from HRANHSUnittests.HRANHSConstantsTests import HRANHSConstantsTests
from HRANHSUnittests.HRANHSTestCases import HRANHSTestCases
from api.HRAModels import MedicineAsset
from api.HRARequests import UpdateMedicineAsset
class HRANHSFrontendTests:
    @staticmethod
    def test_assets_jwt_auth(headers):
        response = requests.get(f"{HRANHSConstantsTests.URI}/assets",headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to access assets page. Status code: {response.status_code}")
        return response