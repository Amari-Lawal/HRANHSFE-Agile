from api.HRANHSDB.HRANHSCRUD import HRANHSCRUD
from api.HRAModels import User,MedicineAsset,Vendor
class HRANHSCreateTables:
    @staticmethod
    def create(hracrud :HRANHSCRUD):
        hracrud.create_table(User.fields_to_tuple(),User.USERSDATATYPES,User.USERSTABLENAME)
        hracrud.create_table(Vendor.fields_to_tuple(),Vendor.VENDORDATATYPES,Vendor.VENDORTABLENAME)   
        hracrud.create_table(MedicineAsset.fields_to_tuple(),MedicineAsset.MEDICINEASSETDATATYPES,MedicineAsset.MEDICINEASSETSTABLENAME)        

