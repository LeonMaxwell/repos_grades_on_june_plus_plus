import datetime
from datetime import timedelta
import calendar

if __name__ == '__main__':
    # Создание объекта даты
    d = datetime.datetime(2022, 10, 2)
    print(d)

    # Расчет между двумя датами
    d1 = datetime.datetime.now()
    print(d1)
    d2 = datetime.datetime(2022, 10, 2)
    print(d2)
    delta = d1 - d2
    print(delta)

    # Получение дат и времени
    date_today = datetime.datetime.today()
    print(date_today)
    print(date_today.combine(date_today.date(), date_today.min.time()))
    print(date_today.combine(date_today.date(), date_today.max.time()))

    # Заглянем в будущее
    print(date_today + timedelta(days=1))
    print(date_today + timedelta(weeks=1))
    date_in_month = calendar.monthrange(date_today.year, date_today.month)[1]
    print(date_today + timedelta(days=date_in_month))
    date_in_years = date_today.replace(year=date_today.year + 1)
    print(date_in_years)
    print(date_in_years.isoweekday())

