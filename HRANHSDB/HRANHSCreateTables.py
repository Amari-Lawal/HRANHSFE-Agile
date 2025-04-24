from HRANHSDB.HRANHSCRUD import HRANHSCRUD
from HRAModels import User,MedicineAsset
class HRANHSCreateTables:
    @staticmethod
    def create(hracrud :HRANHSCRUD):
        hracrud.create_table(User.fields_to_tuple(),User.USERSDATATYPES,User.USERSTABLENAME)
        hracrud.create_table(MedicineAsset.fields_to_tuple(),MedicineAsset.MEDICINEASSETDATATYPES,MedicineAsset.MEDICINEASSETSTABLENAME)    
