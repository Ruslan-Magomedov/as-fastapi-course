from fastapi import APIRouter, HTTPException, status


router = APIRouter(prefix="/auth", tags=["Авторизация и аутентификация"])


@router.post("/register", summary="Регистрация", status_code=status.HTTP_201_CREATED)
async def register_user():
    pass
