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