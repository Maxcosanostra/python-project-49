import random


def get_number_and_even_answer():
    number = random.randint(1, 100)
    return number, 'yes' if number % 2 == 0 else 'no'
