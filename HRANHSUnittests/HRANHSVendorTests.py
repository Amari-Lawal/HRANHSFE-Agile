import requests
from HRANHSUnittests.HRANHSConstantsTests import HRANHSConstantsTests
class HRANHSVendorTests:
    @staticmethod
    def create_vendor(headers):
        response = requests.post(f"{HRANHSConstantsTests.URI}/api/v1/vendors/create_vendor",headers=headers,json={
        "vendor_name": HRANHSConstantsTests.VENDOR_NAME,
        "vendor_address": "123 Industrial Park Road, Springfield, IL 62704",
        "contact_person": "John Doe",
        "contact_number": "+1-555-123-4567",
        "email": "john.doe@abcsupplies.com",
        "status": "active"
        }
                )
        return response.json()
    @staticmethod
    def get_all_vendors(headers):
        response = requests.get(f"{HRANHSConstantsTests.URI}/api/v1/vendors/get_all_vendors",headers=headers)
        return response.json().get("vendors",[])
    @staticmethod
    def get_first_vendor_id(vendors):
        if vendors:
            return vendors[0].get("vendor_id")
        else:
            return None
    @staticmethod
    def get_vendor_from_name(headers):
        response = requests.get(f"{HRANHSConstantsTests.URI}/api/v1/vendors/get_vendor",params={"vendor_name":HRANHSConstantsTests.VENDOR_NAME},headers=headers)
        return response.json()
    @staticmethod
    def get_vendor_from_id(headers,vendor_id):
        response = requests.get(f"{HRANHSConstantsTests.URI}/api/v1/vendors/get_vendor",params={"vendor_id":vendor_id},headers=headers)
        return response.json()
    @staticmethod
    def update_vendor(headers,vendor_id,update_data):
        response = requests.put(f"{HRANHSConstantsTests.URI}/api/v1/vendors/update_vendor/{vendor_id}",headers=headers,json=update_data)
        return response.json()
    @staticmethod
    def delete_vendor(headers,vendor_id):
        response = requests.delete(f"{HRANHSConstantsTests.URI}/api/v1/vendors/delete_vendor/{vendor_id}",headers=headers)
        return response.json()
    