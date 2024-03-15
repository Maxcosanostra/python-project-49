import random
import math


def get_nums_pair_and_gcd():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = "{} {}".format(number1, number2)
    correct_answer = str(math.gcd(number1, number2))
    return question, correct_answer
