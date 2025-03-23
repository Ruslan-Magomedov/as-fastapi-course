from fastapi import FastAPI, Query, Body
import uvicorn


app = FastAPI()
hotels_db = [
    {"id": 1, "hotel_name": "lora", "city": "Moscow"},
    {"id": 2, "hotel_name": "Soma", "city": "Rim"},
    {"id": 3, "hotel_name": "Mica", "city": "Paris"},
    {"id": 4, "hotel_name": "Luo", "city": "Rim"},
]


@app.get("/hotels", summary="get hotels")
def get_hotels(city: str | None = Query(default=None)):
    """ head point for get a hotel or hotels by key city """
    if city is None:
        return hotels_db
    return [hotel for hotel in hotels_db if hotel["city"] == city]


@app.delete("/hotels/{hotel_id}", summary="delete hotel")
def delete_hotel(hotel_id: int):
    """ delete hotel by key hotel_id """
    for index, hotel in enumerate(hotels_db):
        if hotel["id"] == hotel_id:
            hotels_db.pop(index)
            return {"status": 200, "message": "OK"}
    return {"status": 404, "message": "Not Found"}


@app.post("/hotels")
def create_hotel(
        hotel_name: str | None = Body(default=None, embed=True),
        city: str | None = Body(default=None, embed=True)
):
    """ create hotel by keys hotel_name and city """
    if not (hotel_name and city):
        return {"status": 422, "message": "Bad Data"}
    hotels_db.append({
            "id": hotels_db[-1]["id"] + 1,
            "hotel_name": hotel_name,
            "city": city
        })
    return {"status": 200, "message": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
