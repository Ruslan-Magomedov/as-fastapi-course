from sqlalchemy import select, insert, update, delete
from pydantic import BaseModel


class BaseRepositories:
    model = None

    def __init__(self, session):
        self.session = session

    async def get_one(self, **filters):
        statement = select(self.model).filter_by(**filters)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def get_all(self, *args, **kwargs):
        statement = select(self.model)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def get_byfilter(self, **filters):
        statement = select(self.model).filter_by(**filters)
        result = await self.session.execute(statement)
        return result.scalars().one_or_none()

    async def add(self, data: BaseModel):
        statement = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(statement)
        return result.scalars().one()

    async def update(self, data: BaseModel, exclude_unset: bool = False, **filters) -> None:
        statement = update(self.model).filter_by(**filters).values(**data.model_dump(exclude_unset=exclude_unset))
        await self.session.execute(statement)

    async def delete(self, **filters) -> None:
        statement = delete(self.model).filter_by(**filters)
        await self.session.execute(statement)
