from fastapi import Query, APIRouter
from sqlalchemy import insert, select

from src.database import session_maker
from src.models.hotels import HotelsOrm
from src.shemas.hotels import HotelData, HotelDataPatch
from src.api.dependencies import PaginationDep


router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("", summary="get hotels")
async def get_hotels(pagination: PaginationDep,
               location: str | None = Query(None)):
    """ head point for get a hotel or hotels by key location """
    per_page = pagination.per_page or 5
    async with session_maker() as session:
        query = select(HotelsOrm)
        if location:
            query = query.filter_by(location=location)
        query = (
            query
            .limit(per_page)
            .offset(per_page * (pagination.page - 1))
        )
        result = await session.execute(query)
        hotels = result.scalars().all()
        return hotels


@router.post("", summary="create hotel")
async def create_hotel(hotel_data: HotelData):
    """ create hotel by keys title and location """
    if hotel_data.title and hotel_data.location:
        async with session_maker() as session:
            add_hotel_stmt = insert(HotelsOrm).values(**hotel_data.model_dump())
            await session.execute(add_hotel_stmt)
            await session.commit()
            return {"status": 200, "message": "OK"}
    return {"status": 422, "message": "Bad Data"}


# @router.put("/{hotel_id}", summary="edit hotel")
# def edit_hotel(hotel_id: int, hotel_data: HotelData):
#     """ edit hotel by key hotel_id """
#     if hotel_id and hotel_data.hotel_name and hotel_data.city:
#         for index, hotel in enumerate(hotels_db):
#             if hotel["id"] == hotel_id:
#                 hotels_db[index]["hotel_name"] = hotel_data.hotel_name
#                 hotels_db[index]["city"] = hotel_data.city
#                 return {"status": 200, "message": "OK"}
#     return {"status": 422, "message": "Bad Data"}
#
#
# @router.patch("/{hotel_id}", summary="partial edit hotel")
# def partial_edit_hotel(hotel_id: int, hotel_data: HotelDataPatch):
#     """ partial edit hotel by key hotel_id """
#     if hotel_id:
#         for index, hotel in enumerate(hotels_db):
#             if hotel["id"] == hotel_id:
#                 if hotel_data.hotel_name:
#                     hotels_db[index]["hotel_name"] = hotel_data.hotel_name
#                 if hotel_data.city:
#                     hotels_db[index]["city"] = hotel_data.city
#                 return {"status": 200, "message": "OK"}
#     return {"status": 422, "message": "Bad Data"}
#
#
# @router.delete("/{hotel_id}", summary="delete hotel")
# def delete_hotel(hotel_id: int):
#     """ delete hotel by key hotel_id """
#     for index, hotel in enumerate(hotels_db):
#         if hotel["id"] == hotel_id:
#             hotels_db.pop(index)
#             return {"status": 200, "message": "OK"}
#     return {"status": 404, "message": "Not Found"}
