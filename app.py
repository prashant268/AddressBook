# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List
import geopy.distance
from apiModel import *
from db import *
from utils import *
app = FastAPI()



# API endpoints
@app.get("/")
def health():
    return({"msg":"App is working"})
@app.post("/addresses/", response_model=AddressResponse)
def create_address_endpoint(address: AddressCreate, db: Session = Depends(get_db)):
    return create_address(db=db, address=address)

@app.get("/addresses/{address_id}", response_model=AddressResponse)
def read_address_endpoint(address_id: int, db: Session = Depends(get_db)):
    db_address = get_address(db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@app.put("/addresses/{address_id}", response_model=AddressResponse)
def update_address_endpoint(address_id: int, address: AddressUpdate, db: Session = Depends(get_db)):
    db_address = update_address(db=db, address_id=address_id, address=address)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@app.delete("/addresses/{address_id}", response_model=AddressResponse)
def delete_address_endpoint(address_id: int, db: Session = Depends(get_db)):
    db_address = delete_address(db=db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@app.get("/addresses/", response_model=List[AddressResponse])
def read_addresses_within_distance_endpoint(lat: float, lon: float, dist: float, db: Session = Depends(get_db)):
    addresses = get_addresses_within_distance(db=db, latitude=lat, longitude=lon, distance=dist)
    return addresses

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host='0.0.0.0',port=800)