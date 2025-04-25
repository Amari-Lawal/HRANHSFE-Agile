import requests
from typing import Optional
from HRANHSUnittests.HRANHSConstantsTests import HRANHSConstantsTests
from HRANHSUnittests.HRANHSTestCases import HRANHSTestCases
from api.HRAModels import MedicineAsset
from api.HRARequests import HRAUpdateMedicineAsset
class HRANHSAssetsTests:
    @staticmethod
    def create_medicine_asset(headers,asset_data:MedicineAsset):
        response = requests.post(f"{HRANHSConstantsTests.URI}/api/v1/assets/create_medicine_asset",headers=headers,json=asset_data
                )
        return response.json()
    @staticmethod
    def get_all_medicine_assets(headers):
        response = requests.get(f"{HRANHSConstantsTests.URI}/api/v1/assets/get_all_medicine_assets",headers=headers)
        return response.json().get("medicine_assets",[])
    @staticmethod
    def get_medicine_asset(headers,medicine_id:Optional[str]=None):
        if medicine_id:
            response = requests.get(f"{HRANHSConstantsTests.URI}/api/v1/assets/get_medicine_asset",params={"medicine_id":medicine_id},headers=headers)
        else:
            response = requests.get(f"{HRANHSConstantsTests.URI}/api/v1/assets/get_medicine_asset",params={"medicine_asset":HRANHSConstantsTests.MEDICINE_ASSET},headers=headers)
        return response.json().get("medicine_assets",[])
    @staticmethod
    def get_first_asset_id(medicine_assets):
        if medicine_assets:
            return medicine_assets[0].get("medicine_id")
        else:
            return None
    @staticmethod
    def update_medicine_asset(headers,medicine_id:str,asset_data:HRAUpdateMedicineAsset):
        response = requests.put(f"{HRANHSConstantsTests.URI}/api/v1/assets/update_medicine_asset/{medicine_id}",json=asset_data,headers=headers)
        return response.json()
    @staticmethod
    def delete_medicine_asset(headers,medicine_id:str):
        response = requests.delete(f"{HRANHSConstantsTests.URI}/api/v1/assets/delete_medicine_asset/{medicine_id}",headers=headers)
        return response.json()
    @staticmethod
    def get_medicine_asset_by_vendor(headers,vendor_id:str):
        response = requests.get(f"{HRANHSConstantsTests.URI}/api/v1/assets/get_medicine_assets_by_vendor/{vendor_id}",headers=headers)
        return response.json().get("medicine_assets",[])
    