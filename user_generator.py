import random


def generate_email():
    names = [
        "julia",
        "sasha",
        "vadim",
        "bob"
    ]
    lastNames = [
        "sidorov",
        "thecat",
        "ivanov",
        "grigorenko"
    ]
    domens = [
        "yandex.ru",
        "google.com",
        "mail.ru",
        "gmail.com"
    ]
    
    return f"{names[random.randint(0, len(names) - 1)]}_{lastNames[random.randint(0, len(lastNames) - 1)]}_10_{random.randint(100, 999)}@{domens[random.randint(0, len(domens) - 1)]}"