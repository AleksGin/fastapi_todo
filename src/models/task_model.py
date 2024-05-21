
from src.db.db import Model
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey
from src.schemas.task_schema import TaskSchema




class TaskTable(Model):
    __tablename__ = "to-do"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]
    author_id: Mapped[int] = mapped_column(ForeignKey('our_users.id'))


    def to_read_mode(self) -> TaskSchema:
        return TaskSchema(
            id=self.id,
            title=self.title,
            description=self.description,
            author_id=self.author_id
        )
        
        

# Переключить на Postgres