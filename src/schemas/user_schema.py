from pydantic import BaseModel, ConfigDict

class UserSchema(BaseModel): 
    id: int
    name: str # Спросить можно ли было сделать по аналогии с TaskAdd/TaskGet - как-то унаследовать
                             
    model_config = ConfigDict(from_attributes=True)
    
class UserAddSchema(BaseModel):
    name: str
    
    model_config = ConfigDict(from_attributes=True)