from src.db.db import Model
from sqlalchemy.orm import Mapped, mapped_column
from src.schemas.user_schema import UserSchema


class UserTable(Model):
    __tablename__ = "our_users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            name=self.name,
        )
        
        

# Переключить на Postgres