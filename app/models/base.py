from datetime import datetime

from sqlalchemy import Column, Integer, Boolean, DateTime, CheckConstraint

from app.core.base import Base
from app.core.constans import INVEST_AMOUNT_DEFAULT


class Investment(Base):
    __abstract__ = True
    __table_args__ = (
        CheckConstraint("full_amount > 0"),
        CheckConstraint("invested_amount <= full_amount"),
    )

    full_amount = Column(Integer)
    invested_amount = Column(Integer, default=INVEST_AMOUNT_DEFAULT)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)
