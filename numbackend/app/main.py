#from typing import Union
from fastapi import FastAPI,Depends,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
from .import crud
from sqlalchemy.orm import Session
from .database import SessionLocal,engine
import json

app = FastAPI()
origins = ["*"]

def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# class DataItem(BaseModel):
#     Dict[str, Any]

class DataWithIn(BaseModel):
    LineName: str
    Shift: str
    Data: List[Dict]

# class DataArray(BaseModel):
#     data : List[DataWithIn]

# @app.post("/input")
# async def get_input(data: List[DataWithIn],db:Session = Depends(get_db)):
#     print(data)
#     return data

@app.post("/input")  # Change this to POST
async def post_input(data: List[DataWithIn],db: Session = Depends(get_db)):
    try:
        for item in data:
            item.Data = json.dumps(item.Data)
            success = await crud.post_input(db=db, item=item)
            if not success:
                raise HTTPException(status_code=400, detail=f"Error postdate : {e}")
        return {"success": True}
    except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error during post data : {e}")