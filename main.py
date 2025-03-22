from fastapi import FastAPI, Query
import uvicorn


app = FastAPI()
hotels_db = [
    {"id": 1, "title": "lora", "city": "Moscow"},
    {"id": 2, "title": "Soma", "city": "Rim"},
    {"id": 3, "title": "Mica", "city": "Paris"},
    {"id": 4, "title": "Luo", "city": "Rim"},
]


@app.get("/hotels", summary="Получить отели-ль")
def get_hotels(city: str | None = Query(default=None, description="Город")):
    if city is None:
        return hotels_db
    return [hotel for hotel in hotels_db if hotel["city"] == city]


@app.delete("/hotels/{hotel_id}", summary="Удалить отель")
def delete_hotel(hotel_id: int):
    for index, hotel in enumerate(hotels_db):
        if hotel["id"] == hotel_id:
            hotels_db.pop(index)
            return {"status": 200}
    return {"status": 404}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
