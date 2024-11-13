from sqlalchemy import Column, String, Text, CheckConstraint

from app.models.base import Investment


class CharityProject(Investment):
    name = Column(
        String(100),
        unique=True,
        nullable=False,
    )
    description = Column(Text, nullable=False)

    __table_args__ = (
        CheckConstraint("TRIM(name) != ''", name="non_empty_name"),
    )
