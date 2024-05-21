from src.services.task_service import TaskService
from src.services.user_service import UserService
from src.repositories.task_repository import TasksRepository
from src.repositories.user_repository import UserRepository

async def tasks_service():
    return TaskService(TasksRepository())

async def user_service():
    return UserService(UserRepository())