from pydantic import BaseModel, Field


class HotelData(BaseModel):
    hotel_name: str
    city: str


class HotelDataPatch(BaseModel):
    hotel_name: str | None = Field(None)
    city: str | None = Field(None)
