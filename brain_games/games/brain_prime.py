import random


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_number_and_prime_answer():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return number, correct_answer
