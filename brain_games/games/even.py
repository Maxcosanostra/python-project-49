import random
from brain_games.consts import EVEN_INSTRUCTION
from brain_games.engine import run_game


def get_number_and_even_answer():
    number = random.randint(1, 100)
    return number, 'yes' if number % 2 == 0 else 'no'


def run_even_game():
    run_game(get_number_and_even_answer, EVEN_INSTRUCTION)
