#  Константы для моделей
MAX_LENGTH_NAME = 100
INVEST_AMOUNT_DEFAULT = 0


# Литералы ошибок
class ValidationError:
    CHARITY_PROJECT_EXISTS = "Проект с таким именем уже существует!"
    CHARITY_PROJECT_BY_ID_NOT_FOUND = "Объект с айди с номером {} не найден."
    CHARITY_FULL_AMOUNT_ERROR = (
        "Нельзя установить значение full_amount меньше уже вложенной суммы."
    )
    DONT_DELETE_PROJECT_IF_INVEST_EXIST = (
        "В проект были внесены средства, не подлежит удалению!"
    )
    DONT_CHANGE_PROJECT_IF_INVEST_EXIST = (
        "В проект были внесены средства, не подлежит изменению!"
    )
    NAME_REQUIRED = "Поле name обязательно для заполнения."
