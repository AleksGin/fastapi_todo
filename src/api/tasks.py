from typing import Annotated
from fastapi import APIRouter, Depends

from src.api.dependencies import tasks_service
from src.schemas.task_schema import TaskAddSchema
from src.services.task_service import TaskService


router = APIRouter(prefix="/tasks", tags=["Таски"])


@router.post("/tasks")
async def add_task(
    task: Annotated[TaskAddSchema, Depends()],
    tasks_service: Annotated[TaskService, Depends(tasks_service)],
) -> TaskAddSchema:
    task_id = await tasks_service.add_task_service(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks(tasks_service: Annotated[TaskService, Depends(tasks_service)]):
    tasks = await tasks_service.find_all_tasks_service()
    return tasks


@router.delete("/{task_id}")
async def handle_delete_task(
    task_id: int, tasks_service: Annotated[TaskService, Depends(tasks_service)]
) -> str:
    await tasks_service.delete_by_id_service(task_id)
    return f"Задача под номером {task_id} была успешно удалена"
