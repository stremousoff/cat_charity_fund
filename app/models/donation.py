from sqlalchemy import Column, Text, Integer, ForeignKey

from app.models.base import Investment


class Donation(Investment):
    user_id = Column(Integer, ForeignKey("user.id"))
    comment = Column(Text, nullable=True)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"comment={self.name}, "
            f"fully_invested={self.fully_invested}, "
            f"invested_amount={self.invested_amount}, "
            f"user_invest_id={self.user_id}, "
            f"create_date={self.create_date}, "
        )
