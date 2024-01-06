from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import List
from pydantic import BaseModel
from fastapi import HTTPException

# กำหนด class ที่จะเก็บเข้า database ให้ตรงกับที่รับมาจาก backend
class DataItem(BaseModel):
    LineName:str
    Shift:str
    Data:List[dict]

class DatafromDB(BaseModel):
    # id: str
    LineName:str
    Shift:str
    Data:List[dict]
    # created_at: str
    # updated_at: str

class DefectFromDB(BaseModel):
    lineName:str
    Category:str
    Shift:str
    Data:List[dict]


#โครงสร้างภาษา SQL """......"""
async def post_input(item:DataItem,db: Session):
    print(item)
    try:
        stmt = f"""
        INSERT INTO csvtodatabase(line_name, shift, data)
        VALUES (:line_name, :shift, cast(:data AS jsonb))
        """
        res = db.execute(text(stmt),params={"line_name":item.LineName,"shift":item.Shift,"data":item.Data})
        db.commit()
    except Exception as e:
        print(f"Error during post data: {e}")
        raise HTTPException(status_code=400, detail=f"Bad Request: {e}")
    return res


#####################################################
async def get_data(db: Session):
    try:
        stmt = """
        SELECT line_name, shift, data FROM csvtodatabase
        """
        #id, line_name, shift, data, created_at, updated_at
        result = db.execute(text(stmt))
        data = [
            {"line_name": item[0], "shift": item[1], "data": item[2]} for item in result
        ]
        return data
    except Exception as e:
        raise e

######################################################
async def get_linename(db: Session):
    try:
        stmt = """
        SELECT DISTING line_name FROM csvtodatabase
        """
        result = db.execute(text(stmt))
        data = [
            {"line_name": item[0]} for item in result
        ]
        return data
    except Exception as e:
        raise e
    
##################################################

async def get_resultdata(line_name: str, shift: str, db: Session):  ## Add parameters here
    try:
        stmt = """
        SELECT data FROM csvtodatabase
        WHERE line_name = :line_name AND shift = :shift;
        """
        result = db.execute(text(stmt), {"line_name": line_name, "shift": shift})  ## Pass parameters here
        data = [{"data": item[0]} for item in result]
        return data
    except Exception as e:
        raise e

################################################################################################################
################################################################################################################
    
async def post_input2(item:DefectFromDB,db:Session):
    print(item)
    try:
        stmt = f"""
        INSERT INTO defectdatabase(line_name, category, shift, data)
	    VALUES (:line_name, :category, :shift, cast(:data AS jsonb))
        """
        res = db.execute(text(stmt),params={"line_name":item.LineName,"category":item.Category,"shift":item.Shift,"data":item.Data})
        db.commit()
    except Exception as e:
        print(f"Error during post data: {e}")
        raise HTTPException(status_code=400, detail=f"Bad Request: {e}")
    return res

#####################################################
async def get_data2(db: Session):
    try:
        stmt = """
        SELECT line_name, category, shift, data FROM defectdatabase
        """
        #id, line_name, shift, data, created_at, updated_at
        result = db.execute(text(stmt))
        data = [
            {"line_name": item[0], "category": item[1], "shift": item[2], "data": item[3]} for item in result
        ]
        return data
    except Exception as e:
        raise e
#####################################################
async def get_linename2(db: Session):
    try:
        stmt = """
        SELECT DISTING line_name FROM defectdatabase
        """
        result = db.execute(text(stmt))
        data = [
            {"line_name": item[0]} for item in result
        ]
        return data
    except Exception as e:
        raise e
    
async def get_resultdata2(line_name: str,shift:str,category:str, db: Session):  ## Add parameters here
    try:
        stmt = """
        SELECT data FROM defectdatabase
        WHERE line_name = :line_name AND shift = :shift AND category = :category;
        """
        result = db.execute(text(stmt), {"line_name": line_name, "shift": shift,"category":category})  ## Pass parameters here
        data = [{"data": item[0]} for item in result]
        return data
    except Exception as e:
        raise e