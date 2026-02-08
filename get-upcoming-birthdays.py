# Тема 4: Завдання 4
# Максим Канюка
# 08/02/2026

from datetime import datetime, date, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    result = []

    for user in users:
        # 1) parse birthday
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # 2) birthday in the current year
        birthday_this_year = birthday.replace(year=today.year)

        # 3) if already passed, move to next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # 4) check if it's within the next 7 days (including today)
        if today <= birthday_this_year <= end_date:
            congratulation_date = birthday_this_year

            # 5) move weekend поздравлення to Monday
            # weekday(): Mon=0 ... Sat=5 Sun=6
            if congratulation_date.weekday() == 5:      # Saturday
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:    # Sunday
                congratulation_date += timedelta(days=1)

            # 6) add to result
            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result
