from src.models.user_model import UserTable
from src.utils.repository import SQLRepository

class UserRepository(SQLRepository):
    model = UserTable