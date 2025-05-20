from sqlalchemy import select, delete, func

from src.repositories.base import BaseRepositories
from src.models.hotels import HotelsOrm


class HotelsRepositories(BaseRepositories):
    model = HotelsOrm

    async def get_all(self, title, location, limit, offset):
        query = select(HotelsOrm)
        if title:
            query = query.filter(func.lower(HotelsOrm.title).like(f"%{title.lower()}%"))
        if location:
            query = query.filter(func.lower(HotelsOrm.location).like(f"%{location.lower()}%"))
        query = (
            query
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute(query)
        hotels = result.scalars().all()
        return hotels
