from sqlalchemy.orm import sessionmaker, Session
# from pydantic import BaseModel
from db import *
from apiModel import *
import geopy


def get_address(db: Session, address_id: int):
    return db.query(Address).filter(Address.id == address_id).first()

def create_address(db: Session, address: AddressCreate):
    db_address = Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def update_address(db: Session, address_id: int, address: AddressUpdate):
    db_address = get_address(db, address_id)
    if db_address:
        for key, value in address.dict().items():
            setattr(db_address, key, value)
        db.commit()
        db.refresh(db_address)
    return db_address

def delete_address(db: Session, address_id: int):
    db_address = get_address(db, address_id)
    if db_address:
        db.delete(db_address)
        db.commit()
    return db_address

def get_addresses_within_distance(db: Session, latitude: float, longitude: float, distance: float):
    addresses = db.query(Address).all()
    result = []
    for address in addresses:
        addr_coords = (address.latitude, address.longitude)
        if geopy.distance.distance((latitude, longitude), addr_coords).km <= distance:
            result.append(address)
    return result