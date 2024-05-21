from typing import Annotated
from fastapi import APIRouter, Depends

from src.api.dependencies import user_service
from src.schemas.user_schema import UserAddSchema, UserSchema
from src.services.user_service import UserService


router = APIRouter(prefix="/users", tags=["Юзеры"])


@router.post("/tasks")
async def add_user(
    user: Annotated[UserAddSchema, Depends()],
    user_service: Annotated[UserService, Depends(user_service)],
):
    user_id = await user_service.add_one_service(user)
    return {"ok": True, "user_id": user_id}


@router.get("")
async def get_tasks(user_service: Annotated[UserService, Depends(user_service)]):
    users = await user_service.find_all_users_service()
    return users


@router.delete("/{user_id}")
async def handle_delete_user(
    user_id: int, user_service: Annotated[UserService, Depends(user_service)]
) -> str:
    await user_service.delete_by_id_service(user_id)
    return f"Задача под номером {user_id} была успешно удалена"
