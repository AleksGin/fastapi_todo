from abc import ABC, abstractmethod
from sqlalchemy import select, delete, insert
from src.db.db import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError
    
    @abstractmethod
    async def delele_by_id():
        raise NotImplementedError


class SQLRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        self.data = data
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.flush()
            await session.commit()
            return res.scalar_one()

    async def find_all(self):
        async with async_session_maker() as session:
            query = select(self.model)
            result = await session.execute(query)
            result = [row[0].to_read_model() for row in result.all()]
            return result

    async def delele_by_id(self, task_or_user_id: int):
        async with async_session_maker() as session:
            query = delete(self.model).where(self.model.id == task_or_user_id)
            result = await session.execute(query)
            await session.commit()
