from fastapi import Query, Body, APIRouter


router = APIRouter(prefix="/hotels", tags=["Hotels"])
hotels_db = [
    {"id": 1, "hotel_name": "lora", "city": "Moscow"},
    {"id": 2, "hotel_name": "Soma", "city": "Rim"},
    {"id": 3, "hotel_name": "Mica", "city": "Paris"},
    {"id": 4, "hotel_name": "Luo", "city": "Rim"},
]


@router.get("/hotels", summary="get hotels")
def get_hotels(city: str | None = Query(default=None)):
    """ head point for get a hotel or hotels by key city """
    if city is None:
        return hotels_db
    return [hotel for hotel in hotels_db if hotel["city"] == city]


@router.post("/hotels", summary="create hotel")
def create_hotel(
        hotel_name: str | None = Body(default=None, embed=True),
        city: str | None = Body(default=None, embed=True)
):
    """ create hotel by keys hotel_name and city """
    if hotel_name and city:
        hotels_db.append({
                "id": hotels_db[-1]["id"] + 1,
                "hotel_name": hotel_name,
                "city": city
            })
        return {"status": 200, "message": "OK"}
    return {"status": 422, "message": "Bad Data"}


@router.put("/hotels/{hotel_id}", summary="edit hotel")
def edit_hotel(
        hotel_id: int,
        hotel_name: str = Body(embed=True),
        city: str = Body(embed=True)
):
    if hotel_id and hotel_name and city:
        for index, hotel in enumerate(hotels_db):
            if hotel["id"] == hotel_id:
                hotels_db[index]["hotel_name"] = hotel_name
                hotels_db[index]["city"] = city
                return {"status": 200, "message": "OK"}
    return {"status": 422, "message": "Bad Data"}


@router.patch("/hotels/{hotel_id}", summary="partial edit hotel")
def partial_edit_hotel(
        hotel_id: int,
        hotel_name: str | None = Body(default=None, embed=True),
        city: str | None = Body(default=None, embed=True)
):
    if hotel_id:
        for index, hotel in enumerate(hotels_db):
            if hotel["id"] == hotel_id:
                if hotel_name:
                    hotels_db[index]["hotel_name"] = hotel_name
                if city:
                    hotels_db[index]["city"] = city
                return {"status": 200, "message": "OK"}
    return {"status": 422, "message": "Bad Data"}


@router.delete("/hotels/{hotel_id}", summary="delete hotel")
def delete_hotel(hotel_id: int):
    """ delete hotel by key hotel_id """
    for index, hotel in enumerate(hotels_db):
        if hotel["id"] == hotel_id:
            hotels_db.pop(index)
            return {"status": 200, "message": "OK"}
    return {"status": 404, "message": "Not Found"}