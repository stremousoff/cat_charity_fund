from datetime import datetime

from app.models.base import Investment


def make_investments(
    target: Investment, sources: list[Investment]
) -> list[Investment]:
    _object = []
    for source in sources:
        investment_amount = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount,
        )
        for changed_object in (source, target):
            changed_object.invested_amount += investment_amount
            if changed_object.full_amount == changed_object.invested_amount:
                changed_object.fully_invested = True
                changed_object.close_date = datetime.now()
        _object.append(source)
        if target.fully_invested:
            break
    return _object
