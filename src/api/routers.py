from src.api.users import router as users_router
from src.api.tasks import router as tasks_router

all_routers = [
    tasks_router,
    users_router
]