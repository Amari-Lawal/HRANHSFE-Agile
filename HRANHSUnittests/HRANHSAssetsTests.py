import requests
from HRANHSUnittests.HRANHSConstantsTests import HRANHSConstantsTests
class HRANHSAssetsTests:
    @staticmethod
    def create_medicine_asset(headers,vendor_id):
        response = requests.post(f"{HRANHSConstantsTests.URI}/api/v1/assets/create_medicine_asset",headers=headers,json={
                "medicine_asset": HRANHSConstantsTests.MEDICINE_ASSET,
                "description": "Pain reliever and anti-inflammatory",
                "vendor_id": vendor_id,
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
        return response.json()
    @staticmethod
    def get_all_medicine_assets(headers):
        response = requests.get(f"{HRANHSConstantsTests.URI}/api/v1/assets/get_all_medicine_assets",headers=headers)
        return response.json().get("medicine_assets",[])
    @staticmethod
    def get_medicine_asset(headers):
        response = requests.get(f"{HRANHSConstantsTests.URI}/api/v1/assets/get_medicine_asset",params={"medicine_asset":HRANHSConstantsTests.MEDICINE_ASSET},headers=headers)
        return response.json()
    