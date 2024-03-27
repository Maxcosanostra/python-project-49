import random
from brain_games.consts import CALC_INSTRUCTION, OPERATORS
from brain_games.engine import run_game


def get_math_expression_and_result():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(OPERATORS)
    question = f"{num1} {operator} {num2}"
    result = eval(question)
    return question, str(result)


def run_calc_game():
    run_game(get_math_expression_and_result, CALC_INSTRUCTION)
