
from src.utils.repository import AbstractRepository
from src.schemas.task_schema import TaskAddSchema


class TaskService:
    def __init__(self, task_rep: AbstractRepository):
        self.task_rep: AbstractRepository = task_rep
    
    async def add_task_service(self, task: TaskAddSchema) -> int:
        task_dict = task.model_dump()
        task_id = await self.task_rep.add_one(task_dict)
        return task_id 
    
    async def find_all_tasks_service(self):
        tasks = await self.task_rep.find_all()
        return tasks 
    
    async def delete_by_id_service(self, task_id: int):
        await self.task_rep.delele_by_id(task_id)
        return f'Задача под номером {task_id} была успешно удалена'
        