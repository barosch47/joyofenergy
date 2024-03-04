from typing import List

from pydantic import BaseModel


class Readings(BaseModel):
    time: int
    reading: float


class ElectricReading(BaseModel):
    smartMeterId: str
    electricityReadings: List[Readings]


class PricePlanComparisons(BaseModel):
    pricePlanId: str
    pricePlanComparisons: List[dict]

