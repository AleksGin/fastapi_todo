from src.utils.repository import AbstractRepository
from src.schemas.user_schema import UserAddSchema


class UserService:
    def __init__(self, user_rep: AbstractRepository):
        self.user_rep: AbstractRepository = user_rep
        
    
    async def add_one_service(self, user: UserAddSchema):
        user_dict = user.model_dump()
        user_id = await self.user_rep.add_one(user_dict)
        return user_id
    
    async def find_all_users_service(self):
        users = await self.user_rep.find_all()
        return users
    
    async def delete_by_id_service(self, user_id: int):
        await self.user_rep.delele_by_id(user_id)
        return f'Пользователь под id {user_id} успешно удален'
    

        