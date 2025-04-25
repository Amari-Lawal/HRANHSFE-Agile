import requests
from HRANHSUnittests.HRANHSConstantsTests import HRANHSConstantsTests
import unittest
from HRANHSUnittests.HRANHSTestCases import HRANHSTestCases
class HRANHSignupTest:
    @staticmethod
    def signup(self: unittest.TestCase):
        response = requests.post(f"{HRANHSConstantsTests.URI}/api/v1/users/signup",json=HRANHSTestCases.USER_SIGNUP_ADMIN_TEST_CASE)
        self.assertEqual(response.json().get("error"),None)
        self.assertNotEqual(response.json().get("error"),"you have already done this action can't gain tokens.")

        return response