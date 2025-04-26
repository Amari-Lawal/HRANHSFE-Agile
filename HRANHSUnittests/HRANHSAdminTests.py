import requests
from typing import Optional
from HRANHSUnittests.HRANHSConstantsTests import HRANHSConstantsTests
from HRANHSUnittests.HRANHSTestCases import HRANHSTestCases
from api.HRAModels import MedicineAsset
from api.HRARequests import UpdateMedicineAsset
class HRANHSAdminTests:
    @staticmethod
    def delete_all_data_from_tables(headers):
        response = requests.delete(f"{HRANHSConstantsTests.PUBLIC_URI}/api/v1/admin/delete_all_data_from_tables",headers=headers)
        return response.json()