from fastapi import FastAPI
import uvicorn

from src.api.hotels import router as router_hotels  # роутер отелей


app = FastAPI()
app.include_router(router_hotels)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
