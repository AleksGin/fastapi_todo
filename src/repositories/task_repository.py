from src.models.task_model import TaskTable
from src.utils.repository import SQLRepository

class TasksRepository(SQLRepository):
    model = TaskTable

