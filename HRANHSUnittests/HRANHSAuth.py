import json
import requests
import unittest
import sys

from HRANHSUnittests.HRANHSLoginTest import HRANHSLoginTest
from HRANHSUnittests.HRANHSignupTest import HRANHSignupTest
from HRANHSUnittests.HRANHSAssetsTests import HRANHSAssetsTests
from HRANHSUnittests.HRANHSConstantsTests import HRANHSConstantsTests
from HRANHSUnittests.HRANHSVendorTests import HRANHSVendorTests
from HRANHSUnittests.HRANHSRolesTest import HRANHSRolesTest
from HRANHSUnittests.HRANHSTestCases import HRANHSTestCases
class HRANHSAuth(unittest.TestCase):


    def test_signup(self):
        HRANHSignupTest.signup(self)
    def test_login(self):

        HRANHSignupTest.signup(self)

        HRANHSLoginTest.login()

    def test_create_vendor(self):

        HRANHSignupTest.signup(self)

        headers = HRANHSLoginTest.login()

        HRANHSVendorTests.create_vendor(headers)


    def test_get_user_role(self):
        HRANHSignupTest.signup(self)
        headers = HRANHSLoginTest.login()
        HRANHSRolesTest.get_user_role(headers)

    def test_create_asset(self):

        HRANHSignupTest.signup(self)

        headers = HRANHSLoginTest.login()

        HRANHSVendorTests.create_vendor(headers)

        vendors = HRANHSVendorTests.get_all_vendors(headers)

        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)
        HRANHSTestCases.POST_ASSET_TEST_CASE["vendor_id"] = vendor_id
        HRANHSAssetsTests.create_medicine_asset(headers,HRANHSTestCases.POST_ASSET_TEST_CASE)

    def test_get_all_medicine_assets(self):
        HRANHSignupTest.signup(self)

        headers = HRANHSLoginTest.login()

        HRANHSVendorTests.create_vendor(headers)

        vendors = HRANHSVendorTests.get_all_vendors(headers)

        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)

        HRANHSTestCases.POST_ASSET_TEST_CASE["vendor_id"] = vendor_id
        HRANHSAssetsTests.create_medicine_asset(headers,HRANHSTestCases.POST_ASSET_TEST_CASE)

        HRANHSAssetsTests.get_all_medicine_assets(headers)

    def test_get_medicine_asset(self):

        HRANHSignupTest.signup(self)

        headers = HRANHSLoginTest.login()

        HRANHSVendorTests.create_vendor(headers)

        vendors = HRANHSVendorTests.get_all_vendors(headers)

        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)

        HRANHSTestCases.POST_ASSET_TEST_CASE["vendor_id"] = vendor_id
        HRANHSAssetsTests.create_medicine_asset(headers,HRANHSTestCases.POST_ASSET_TEST_CASE)

        HRANHSAssetsTests.get_medicine_asset(headers)

    def test_get_vendor_from_name(self):

        HRANHSignupTest.signup(self)

        headers = HRANHSLoginTest.login()

        HRANHSVendorTests.create_vendor(headers)

        vendors = HRANHSVendorTests.get_all_vendors(headers)

        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)

        HRANHSTestCases.POST_ASSET_TEST_CASE["vendor_id"] = vendor_id
        HRANHSAssetsTests.create_medicine_asset(headers,HRANHSTestCases.POST_ASSET_TEST_CASE)

        

        HRANHSVendorTests.get_vendor_from_name(headers)

    def test_get_vendor_from_id(self):
        
        HRANHSignupTest.signup(self)
        
        headers = HRANHSLoginTest.login()

        HRANHSVendorTests.create_vendor(headers)

        vendors = HRANHSVendorTests.get_all_vendors(headers)

        vendor_id = HRANHSVendorTests.get_first_vendor_id(vendors)

        HRANHSTestCases.POST_ASSET_TEST_CASE["vendor_id"] = vendor_id
        HRANHSAssetsTests.create_medicine_asset(headers,HRANHSTestCases.POST_ASSET_TEST_CASE)

        response = HRANHSVendorTests.get_vendor_from_id(headers,vendor_id)
    def test_update_medicine_asset(self):
        HRANHSignupTest.signup(self)

        headers = HRANHSLoginTest.login()

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






if __name__ == "__main__":
    unittest.main()