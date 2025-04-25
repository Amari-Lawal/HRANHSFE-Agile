import json
import requests
import unittest
import sys

from HRANHSUnittests.HRANHSAuthTest import HRANHSAuthTest
from HRANHSUnittests.HRANHSAssetsTests import HRANHSAssetsTests
from HRANHSUnittests.HRANHSConstantsTests import HRANHSConstantsTests
from HRANHSUnittests.HRANHSVendorTests import HRANHSVendorTests
from HRANHSUnittests.HRANHSAuthTest import HRANHSAuthTest
from HRANHSUnittests.HRANHSTestCases import HRANHSTestCases
from HRANHSUnittests.HRANHSAdminTests import HRANHSAdminTests
class HRANHSUnittests(unittest.TestCase):


    def test_signup(self):
        HRANHSAuthTest.signup(self)
    def test_login(self):

        HRANHSAuthTest.signup(self)

        headers = HRANHSAuthTest.login()
        HRANHSAdminTests.delete_all_data_from_tables(headers)

    def test_create_vendor(self):

        HRANHSAuthTest.signup(self)

        headers = HRANHSAuthTest.login()

        HRANHSVendorTests.create_vendor(headers)
        HRANHSAdminTests.delete_all_data_from_tables(headers)


    def test_get_user_data(self):
        HRANHSAuthTest.signup(self)
        headers = HRANHSAuthTest.login()
        user_data = HRANHSAuthTest.get_user_data(headers)
        HRANHSAdminTests.delete_all_data_from_tables(headers)

    def test_create_asset(self):

        HRANHSAuthTest.signup(self)

        headers = HRANHSAuthTest.login()

        HRANHSVendorTests.create_vendor(headers)

        vendors = HRANHSVendorTests.get_all_vendors(headers)

        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)
        HRANHSTestCases.POST_ASSET_TEST_CASE["vendor_id"] = vendor_id
        HRANHSAssetsTests.create_medicine_asset(headers,HRANHSTestCases.POST_ASSET_TEST_CASE)
        HRANHSAdminTests.delete_all_data_from_tables(headers)

    def test_get_all_medicine_assets(self):
        HRANHSAuthTest.signup(self)

        headers = HRANHSAuthTest.login()

        HRANHSVendorTests.create_vendor(headers)

        vendors = HRANHSVendorTests.get_all_vendors(headers)

        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)

        HRANHSTestCases.POST_ASSET_TEST_CASE["vendor_id"] = vendor_id
        HRANHSAssetsTests.create_medicine_asset(headers,HRANHSTestCases.POST_ASSET_TEST_CASE)

        HRANHSAssetsTests.get_all_medicine_assets(headers)
        HRANHSAdminTests.delete_all_data_from_tables(headers)

    def test_get_medicine_asset(self):

        HRANHSAuthTest.signup(self)

        headers = HRANHSAuthTest.login()

        HRANHSVendorTests.create_vendor(headers)

        vendors = HRANHSVendorTests.get_all_vendors(headers)

        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)

        HRANHSTestCases.POST_ASSET_TEST_CASE["vendor_id"] = vendor_id
        HRANHSAssetsTests.create_medicine_asset(headers,HRANHSTestCases.POST_ASSET_TEST_CASE)

        HRANHSAssetsTests.get_medicine_asset(headers)
        HRANHSAdminTests.delete_all_data_from_tables(headers)

    def test_get_vendor_from_name(self):

        HRANHSAuthTest.signup(self)

        headers = HRANHSAuthTest.login()

        HRANHSVendorTests.create_vendor(headers)

        vendors = HRANHSVendorTests.get_all_vendors(headers)

        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)

        HRANHSTestCases.POST_ASSET_TEST_CASE["vendor_id"] = vendor_id
        HRANHSAssetsTests.create_medicine_asset(headers,HRANHSTestCases.POST_ASSET_TEST_CASE)

        

        HRANHSVendorTests.get_vendor_from_name(headers)
        HRANHSAdminTests.delete_all_data_from_tables(headers)

    def test_get_vendor_from_id(self):
        
        HRANHSAuthTest.signup(self)
        
        headers = HRANHSAuthTest.login()

        HRANHSVendorTests.create_vendor(headers)

        vendors = HRANHSVendorTests.get_all_vendors(headers)

        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)

        HRANHSTestCases.POST_ASSET_TEST_CASE["vendor_id"] = vendor_id
        HRANHSAssetsTests.create_medicine_asset(headers,HRANHSTestCases.POST_ASSET_TEST_CASE)

        response = HRANHSVendorTests.get_vendor_from_id(headers,vendor_id)
        HRANHSAdminTests.delete_all_data_from_tables(headers)
    def test_update_medicine_asset(self):
        HRANHSAuthTest.signup(self)

        headers = HRANHSAuthTest.login()

        HRANHSVendorTests.create_vendor(headers)

        vendors = HRANHSVendorTests.get_all_vendors(headers)

        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)

        HRANHSTestCases.POST_ASSET_TEST_CASE["vendor_id"] = vendor_id
        HRANHSAssetsTests.create_medicine_asset(headers,HRANHSTestCases.POST_ASSET_TEST_CASE)
        medical_assets = HRANHSAssetsTests.get_medicine_asset(headers)
        medicine_id = HRANHSAssetsTests.get_first_asset_id(medical_assets)
        #print(medicine_id)
        for update_case in HRANHSTestCases.UPDATE_ASSET_TEST_CASES:
            response = HRANHSAssetsTests.update_medicine_asset(headers,medicine_id,update_case)
            #print(response)
        medical_assets = HRANHSAssetsTests.get_medicine_asset(headers,medicine_id=medicine_id)
        #print(medical_assets)
        HRANHSAdminTests.delete_all_data_from_tables(headers)
    def test_delete_medicine_asset(self):
        HRANHSAuthTest.signup(self)

        headers = HRANHSAuthTest.login()

        HRANHSVendorTests.create_vendor(headers)

        vendors = HRANHSVendorTests.get_all_vendors(headers)

        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)

        HRANHSTestCases.POST_ASSET_TEST_CASE["vendor_id"] = vendor_id
        HRANHSAssetsTests.create_medicine_asset(headers,HRANHSTestCases.POST_ASSET_TEST_CASE)
        medical_assets = HRANHSAssetsTests.get_medicine_asset(headers)
    
        medicine_id = HRANHSAssetsTests.get_first_asset_id(medical_assets)
        response = HRANHSAssetsTests.delete_medicine_asset(headers,medicine_id)
        medical_assets = HRANHSAssetsTests.get_medicine_asset(headers)
        medicine_id = HRANHSAssetsTests.get_first_asset_id(medical_assets)
        self.assertEqual(medicine_id,None)
        HRANHSAdminTests.delete_all_data_from_tables(headers)
    def test_delete_vendor(self):
        HRANHSAuthTest.signup(self)

        headers = HRANHSAuthTest.login()

        HRANHSVendorTests.create_vendor(headers)

        vendors = HRANHSVendorTests.get_all_vendors(headers)

        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)
        response = HRANHSVendorTests.delete_vendor(headers,vendor_id)
        vendors = HRANHSVendorTests.get_all_vendors(headers)

        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)
        self.assertEqual(vendor_id,None)
        HRANHSAdminTests.delete_all_data_from_tables(headers)
    def test_delete_vendor_check_assets(self):
        HRANHSAuthTest.signup(self)

        headers = HRANHSAuthTest.login()

        HRANHSVendorTests.create_vendor(headers)

        vendors = HRANHSVendorTests.get_all_vendors(headers)

        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)
        HRANHSTestCases.POST_ASSET_TEST_CASE["vendor_id"] = vendor_id
        HRANHSAssetsTests.create_medicine_asset(headers,HRANHSTestCases.POST_ASSET_TEST_CASE)
        
        medical_assets = HRANHSAssetsTests.get_medicine_asset_by_vendor(headers,vendor_id)
        medicine_id = HRANHSAssetsTests.get_first_asset_id(medical_assets)
        response = HRANHSVendorTests.delete_vendor(headers,vendor_id)
        medical_assets = HRANHSAssetsTests.get_medicine_asset_by_vendor(headers,vendor_id)
        self.assertEqual(medical_assets,[])
        HRANHSAdminTests.delete_all_data_from_tables(headers)
    def test_update_vendor(self):
        HRANHSAuthTest.signup(self)

        headers = HRANHSAuthTest.login()

        HRANHSVendorTests.create_vendor(headers)

        vendors = HRANHSVendorTests.get_all_vendors(headers)

        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)
        for update_case in HRANHSTestCases.UPDATE_VENDOR_TEST_CASES:
            response = HRANHSVendorTests.update_vendor(headers,vendor_id,update_case)
            #print(response)
        vendors = HRANHSVendorTests.get_all_vendors(headers)
        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)
        HRANHSAdminTests.delete_all_data_from_tables(headers)
        #print(vendor_id)
    def test_update_user_info(self):
        HRANHSAuthTest.signup(self)

        headers = HRANHSAuthTest.login()

        HRANHSVendorTests.create_vendor(headers)

        user_data = HRANHSAuthTest.get_user_data(headers)
        #print(user_data)
        for update_case in HRANHSTestCases.UPDTAE_USER_TEST_CASE:
            #print(update_case)
            response = HRANHSAuthTest.update_user(headers,user_data.user_id,update_case)
            #print(response)
            print(response)
        all_user_data = HRANHSAuthTest.get_all_user_data(headers)
        print(all_user_data)

        HRANHSAdminTests.delete_all_data_from_tables(headers)

        #print(vendor_id)
    





if __name__ == "__main__":
    unittest.main()