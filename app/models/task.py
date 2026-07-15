from datetime import datetime, timezone

from sqlalchemy import String, DateTime, ForeignKey, Text, Enum, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.enums import TaskStatus, TaskPriority


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"), nullable=False)

    # Auto-relacionamento: uma tarefa pode ter uma tarefa "pai".
    # Se parent_task_id for None, é uma tarefa principal; caso contrário, é subtarefa.
    parent_task_id: Mapped[int | None] = mapped_column(
        ForeignKey("tasks.id"), nullable=True
    )

    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus), default=TaskStatus.PENDING, nullable=False
    )
    priority: Mapped[TaskPriority] = mapped_column(
        Enum(TaskPriority), default=TaskPriority.MEDIUM, nullable=False
    )

    # Tempo estimado em minutos (mais fácil de agregar/comparar que texto livre)
    estimated_minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    due_date: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    # Campos usados na Etapa 6 (Dashboard de produtividade)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    project: Mapped["Project"] = relationship(back_populates="tasks")

    # Relacionamento pai/filho para subtarefas
    parent_task: Mapped["Task | None"] = relationship(
        remote_side=[id], back_populates="subtasks"
    )
    subtasks: Mapped[list["Task"]] = relationship(
        back_populates="parent_task", cascade="all, delete-orphan"
    )
