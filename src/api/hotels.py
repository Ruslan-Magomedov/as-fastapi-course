from fastapi import Query, APIRouter

from src.database import session_maker
from src.shemas.hotels import HotelData, HotelDataPatch
from src.api.dependencies import PaginationDep
from src.repositories.hotels import HotelsRepositories


router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("/{hotel_id}", summary="get hotel")
async def get_hotel(hotel_id: int):
    """ head point for get a hotel by id """
    async with session_maker() as session:
        return await HotelsRepositories(session).get_one(hotel_id=hotel_id)


@router.get("", summary="get hotels")
async def get_hotels(pagination: PaginationDep,
                     title: str | None = Query(None),
                     location: str | None = Query(None)):
    """ head point for get a hotel or hotels by key title, location """
    per_page = pagination.per_page or 5
    async with session_maker() as session:
        return await HotelsRepositories(session).get_all(
            title=title,
            location=location,
            limit=per_page,
            offset=per_page * (pagination.page - 1)
        )


@router.post("", summary="create hotel")
async def create_hotel(hotel_data: HotelData):
    """ create hotel by keys title and location """
    if hotel_data.title and hotel_data.location:
        async with session_maker() as session:
            hotel_temp = await HotelsRepositories(session).add(hotel_data)
            await session.commit()
        return {"status": 200, "data": hotel_temp}
    return {"status": 422, "message": "Bad Data"}


@router.put("/{hotel_id}", summary="edit hotel")
async def edit_hotel(hotel_id: int, hotel_data: HotelData):
    """ edit hotel by key hotel_id """
    async with session_maker() as session:
        await HotelsRepositories(session).update(data=hotel_data, hotel_id=hotel_id)
        await session.commit()
    return {"status": 200, "message": "OK"}


@router.patch("/{hotel_id}", summary="partial edit hotel")
async def partial_edit_hotel(hotel_id: int, hotel_data: HotelDataPatch):
    """ partial edit hotel by key hotel_id """
    async with session_maker() as session:
        await HotelsRepositories(session).update(data=hotel_data, exclude_unset=True, hotel_id=hotel_id)
        await session.commit()
    return {"status": 200, "message": "OK"}


@router.delete("/{hotel_id}", summary="delete hotel")
async def delete_hotel(hotel_id: int):
    """ delete hotel by key hotel_id """
    async with session_maker() as session:
        await HotelsRepositories(session).delete(hotel_id=hotel_id)
        await session.commit()
    return {"status": 200, "message": "OK"}
