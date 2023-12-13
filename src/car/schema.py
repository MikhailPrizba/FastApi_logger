from datetime import datetime

from pydantic import BaseModel


class CarCreate(BaseModel):
    mark: str
    models: str
    car_type: str
    color: str
    descriptions: str
    max_price: int
    is_active: bool
