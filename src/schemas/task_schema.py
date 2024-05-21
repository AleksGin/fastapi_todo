from pydantic import BaseModel, ConfigDict


    
class TaskSchema(BaseModel):
    id: int
    title: str
    description: str | None = None
    author_id: int
    
    model_config = ConfigDict(from_attributes=True)
    
class TaskAddSchema(BaseModel):
    title: str
    author_id: int
    description: str | None = None
    
    model_config = ConfigDict(from_attributes=True)
    
class TaskId(BaseModel):
    ok: bool = True
    task_id: int
    
    