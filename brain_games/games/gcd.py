import random
import math
from brain_games.engine import run_game
from brain_games.consts import GCD_INSTRUCTION


def get_nums_pair_and_gcd():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"{number1} {number2}"
    correct_answer = str(math.gcd(number1, number2))
    return question, correct_answer


def run_gcd_game():
    run_game(get_nums_pair_and_gcd, GCD_INSTRUCTION)
