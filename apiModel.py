from pydantic import BaseModel
class AddressBase(BaseModel):
    street: str
    city: str
    state: str
    country: str
    latitude: float
    longitude: float

class AddressCreate(AddressBase):
    pass

class AddressUpdate(AddressBase):
    pass

class AddressResponse(AddressBase):
    id: int

    class Config:
        orm_mode = True
