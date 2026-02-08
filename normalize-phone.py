# Тема 4: Завдання 3
# Максим Канюка
# 08/02/2026

import re


def normalize_phone(phone_number: str) -> str:
    # remove all characters except digits and '+'
    cleaned = re.sub(r"[^\d+]", "", phone_number)

    # normalize country code
    if cleaned.startswith("+"):
        return cleaned
    elif cleaned.startswith("380"):
        return "+" + cleaned
    else:
        return "+38" + cleaned
