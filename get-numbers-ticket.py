# Тема 4: Завдання 2
# Максим Канюка
# 08/02/2026

import random

def get_numbers_ticket(min, max, quantity):
    # validate input
    if (
        min < 1
        or max > 1000
        or min >= max
        or quantity <= 0
        or quantity > (max - min + 1)
    ):
        return []

    # generate unique random numbers
    numbers = random.sample(range(min, max + 1), quantity)

    # return sorted result
    return sorted(numbers)

