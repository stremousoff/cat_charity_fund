from sqlalchemy import Column, String, Text, CheckConstraint

from app.core.constans import ValidationError, MAX_LENGTH_NAME
from app.models.base import Investment


class CharityProject(Investment):
    name = Column(
        String(MAX_LENGTH_NAME),
        unique=True,
        nullable=False,
    )
    description = Column(Text, nullable=False)

    __table_args__ = (
        CheckConstraint(
            "TRIM(name) != ''", name=ValidationError.NAME_REQUIRED
        ),
    )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"name={self.name}, "
            f"fully_invested={self.fully_invested}, "
            f"invested_amount={self.invested_amount}, "
            f"create_date={self.create_date}, "
        )
