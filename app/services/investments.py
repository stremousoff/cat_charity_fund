from datetime import datetime

from app.models.base import Investment


def make_investments(
    investment_object: Investment, sources_investments: list[Investment]
) -> list[Investment]:
    change_objects = []
    for source_investment in sources_investments:
        required_amount = min(
            source_investment.full_amount - source_investment.invested_amount,
            investment_object.full_amount - investment_object.invested_amount,
        )
        for changed_object in (source_investment, investment_object):
            changed_object.invested_amount += required_amount
            if changed_object.full_amount == changed_object.invested_amount:
                changed_object.fully_invested = True
                changed_object.close_date = datetime.now()
        change_objects.append(changed_object)
        if investment_object.fully_invested:
            break
    return change_objects
