from sqlalchemy import Column, Text, Integer, ForeignKey

from app.models.base import Investment


class Donation(Investment):
    user_id = Column(Integer, ForeignKey("user.id"))
    comment = Column(Text, nullable=True)
