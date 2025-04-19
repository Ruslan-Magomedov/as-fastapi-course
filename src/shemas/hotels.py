from pydantic import BaseModel, Field


class HotelData(BaseModel):
    title: str
    location: str


class HotelDataPatch(BaseModel):
    title: str | None = Field(None)
    location: str | None = Field(None)
