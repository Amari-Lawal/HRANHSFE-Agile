from HRANHSDB.HRANHSCRUD import HRANHSCRUD
from HRAModels import User
class HRANHSCreateTables:
    @staticmethod
    def create(hracrud :HRANHSCRUD):
        hracrud.create_table(User.fields_to_tuple(),User.USERSDATATYPES,User.USERSTABLENAME)
