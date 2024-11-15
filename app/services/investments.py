from datetime import datetime

from app.models.base import Investment


def limit_invested_amount(investment: Investment, amount: int) -> int:
    return min(investment.full_amount, investment.invested_amount + amount)


def update_investment(
    target: Investment, source: Investment, amount: int
) -> None:
    target.invested_amount = limit_invested_amount(target, amount)
    source.invested_amount = limit_invested_amount(source, amount)
    for investment in [target, source]:
        if investment.invested_amount >= investment.full_amount:
            investment.fully_invested = True
            investment.close_date = datetime.now()


def make_investments(
    target: Investment, sources: list[Investment]
) -> list[Investment]:
    change_object = []
    for source in sources:
        available_source_amount = source.full_amount - source.invested_amount
        required_target_amount = target.full_amount - target.invested_amount
        if available_source_amount >= required_target_amount:
            update_investment(target, source, required_target_amount)
            change_object.append(source)
            change_object.append(target)
            return change_object
        else:
            update_investment(target, source, available_source_amount)
            source.close_date = datetime.now()
            change_object.append(source)
            continue
    return change_object
