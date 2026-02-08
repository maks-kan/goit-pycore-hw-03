# Тема 4: Завдання 1
# Максим Канюка
# 08/02/2026

from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        # convert string to datetime object
        given_date = datetime.strptime(date, "%Y-%m-%d").date()

        # get today's date (without time)
        today = datetime.today().date()

        # calculate difference
        delta = today - given_date

        return delta.days

    except ValueError:
        raise ValueError("Date must be in format YYYY-MM-DD")
