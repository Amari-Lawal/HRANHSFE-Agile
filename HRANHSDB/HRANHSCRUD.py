import base64
from HRANHSDB.HRANHSSQL import HRANHSSQL

class HRANHSCRUD:
    def __init__(self) -> None:
        self.hranhssql = HRANHSSQL()
 
    def create_table(self,fields:tuple,types :tuple,table: str):
        if type(fields) == tuple:
            fieldlist = [f"{field} {typestr}"for field,typestr in zip(fields,types)]
            fieldstr = ', '.join(fieldlist)
            try:
                result = self.hranhssql.run_command(f"CREATE TABLE IF NOT EXISTS {table} ({fieldstr});",self.hranhssql.fetch)
            except Exception as ex:
                return {"error":f"{type(ex)},{ex}"}

        else:
            fieldstr = f"{fields} {types}"
            try:
                result = self.hranhssql.run_command(f"CREATE TABLE IF NOT EXISTS {table} ({fieldstr});",self.hranhssql.fetch)
            except Exception as ex:
                return {"error":f"{type(ex)},{ex}"}

    def post_data(self,fields:tuple,values:tuple,table:str):

            valuestr= str(tuple("?" for i in values)).replace("'","",100)
            fieldstr = str(tuple(i for i in fields)).replace("'","",100)
            
            if len(fields) == 1:
                fieldstr = fieldstr.replace(",","",100)
                valuestr = valuestr.replace(",","",100)
            #print(f"INSERT INTO {table} {fieldstr} VALUES {valuestr};")

            #values = tuple(map(convert_to_hex,values))

            result = self.hranhssql.run_command(f"INSERT INTO {table} {fieldstr} VALUES {valuestr};",self.hranhssql.fetch,datatuple=values)

    
    def get_data(self,fields:tuple,table:str,condition=None,getamount:int=1000):
    
        if len(fields) != 1:
            fieldlist = [f"{field}" for field in fields]
            fieldstr = ', '.join(fieldlist) 
        else:
            fieldstr = fields[0]
        
            #fieldstr = fieldstr.replace(", ","",100)
        if condition:
            #print(f"""SELECT {fieldstr} FROM {table} WHERE {condition};""")
            result = self.hranhssql.run_command(f"""SELECT {fieldstr} FROM {table} WHERE {condition} LIMIT {str(getamount)};""",self.hranhssql.fetch)
            if len(result) == 0:
                return False
            elif len(result) != 0 and type(result) == list:
                result = self.tuple_to_json(fields,result)
                return result
            else:
                return {"error":"error syntax error.","error":result}
        else:
            result = self.hranhssql.run_command(f"""SELECT {fieldstr} FROM {table} LIMIT {str(getamount)};""",self.hranhssql.fetch)
            if len(result) == 0:
                return False
            elif len(result) != 0 and type(result) == list:
                result = self.tuple_to_json(fields,result)
                return result
            else:
                return {"error":"error syntax error.","error":result}
    def update_data(self,fieldstoupdate:tuple,values:tuple,table=str,condition=str):
        if len(fieldstoupdate) > 1:
            updatelist = []
            for field,value in zip(fieldstoupdate,values):
                if type(value) != str:
                    fieldstr = f"{field} = {value}"
                    updatelist.append(fieldstr)

                else:
                    value = value.replace("'","''",1000000)
                    fieldstr = f"{field} = '{value}'"
                    updatelist.append(fieldstr)
            updatestr = ', '.join(updatelist)
            #print(f"UPDATE {table} SET {updatestr} WHERE {condition};")
            result = self.hranhssql.run_command(f"UPDATE {table} SET {updatestr} WHERE {condition};",self.hranhssql.fetch)
            if len(result) == 0:
                return True
            else:
                return False
        else:          
            if type(values[0]) != str:
                updatestr = f"{fieldstoupdate[0]} = {values[0]}"
            else:
                value = values[0].replace("'","''",1000000)
                updatestr = f"{fieldstoupdate[0]} = '{value}'"
            #print(f"UPDATE {table} SET {updatestr} WHERE {condition};")
            result = self.hranhssql.run_command(f"UPDATE {table} SET {updatestr} WHERE {condition};",self.hranhssql.fetch)


    def delete_data(self,table:str,condition:str):
        field_name = condition.split("=")[0].strip()
        result = self.hranhssql.run_command(f"DELETE FROM {table} WHERE {condition};",self.hranhssql.fetch)
        
    def check_exists(self,fields:tuple,table:str,condition=None):
        if len(fields) != 1:
            fieldlist = [f"{field}" for field in fields]
            fieldstr = ', '.join(fieldlist) 
        else:
            fieldstr = fields[0]
        
            #fieldstr = fieldstr.replace(", ","",100)
        if condition:
            #print(f"""SELECT {fieldstr} FROM {table} WHERE {condition};""")
            result = self.hranhssql.run_command(f"""SELECT {fieldstr} FROM {table} WHERE {condition};""",self.hranhssql.check_exists)
            if result == True or result == False:
                return result
            else:
                return {"message":"syntax error or table doesn't exist.","error":result}
                
        else:
            result = self.hranhssql.run_command(f"""SELECT {fieldstr} FROM {table};""",self.hranhssql.check_exists)
            if result == True or result == False:
                return result
            else:
                return {"message":"syntax error or table doesn't exist.","error":result}

    def tuple_to_json(self,fields:tuple,result:tuple):
        if type(result[0]) == tuple:
            final_result = []
            for entry in result:
                entrydict = dict(zip(fields,entry))
                final_result.append(entrydict)
            return final_result
        elif type(result[0]) == str:
            final_result = dict(zip(fields,result))
            return final_result 
        
    def json_to_tuple(self,json:dict):
        keys = tuple(json.keys())
        values = tuple(json.values())
        return keys,values
