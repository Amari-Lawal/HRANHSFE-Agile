from api.HRANHSDB.HRANHSCRUD import HRANHSCRUD
from api.HRANHSDB.HRANHSHash import HRANHSHash
from api.HRANHSJWT import HRANHSJWT
from api.HRANHSDB import HRANHSCreateTables
hracrud = HRANHSCRUD()
hranhsjwt = HRANHSJWT(hracrud)
HRANHSCreateTables.create(hracrud)