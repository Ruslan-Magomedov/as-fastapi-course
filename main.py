from fastapi import FastAPI
import uvicorn

from routers.hotels import router as router_hotels


app = FastAPI()
app.include_router(router_hotels)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
