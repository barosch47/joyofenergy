from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Path

from src.controller.models import ElectricReading, Readings
from src.repository.electricity_reading_repository import ElectricityReadingRepository
from src.service.electricity_reading_service import ElectricityReadingService

repository = ElectricityReadingRepository()
service = ElectricityReadingService(repository)

router = APIRouter(prefix="/readings", tags=["Readings"])


@router.post(
    "/store",
    response_model=ElectricReading,
    description="Store Readings",
)
def store(data: ElectricReading):
    service.store_reading(data.model_dump(mode="json"))
    return data


@router.get(
    "/read/{smart_meter_id}",
    response_model=List[Readings],
    description="Get Stored Readings",
)
def read(smart_meter_id: str = Path(examples=["smart-meter-0"])):
    readings = service.retrieve_readings_for(smart_meter_id)
    if len(readings) < 1:
        return HTTPStatus.NOT_FOUND
    else:
        return [r.to_json() for r in readings]
