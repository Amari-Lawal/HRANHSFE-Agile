from HRANHSDB.HRANHSCRUD import HRANHSCRUD
from HRAModels import User,MedicineAsset,Vendor
class HRANHSCreateTables:
    @staticmethod
    def create(hracrud :HRANHSCRUD):
        hracrud.hranhssql.run_command("PRAGMA foreign_keys = ON;",hracrud.hranhssql.fetch) # Sets foreign keys to be on.
        hracrud.create_table(User.fields_to_tuple(),User.USERSDATATYPES,User.USERSTABLENAME)
        hracrud.create_table(Vendor.fields_to_tuple(),Vendor.VENDORDATATYPES,Vendor.VENDORTABLENAME)   
        hracrud.create_table(MedicineAsset.fields_to_tuple(),MedicineAsset.MEDICINEASSETDATATYPES,MedicineAsset.MEDICINEASSETSTABLENAME)        

