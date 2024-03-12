import random
import operator
from ..engine.engine import welcome_player, test_game


OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(list(OPERATORS.keys()))
    question = f"{num1} {operator} {num2}"
    correct_answer = str(OPERATORS[operator](num1, num2))
    return question, correct_answer


def check_answer(my_answer, correct_answer):
    return my_answer == correct_answer


def main():
    name = welcome_player()
    print("What is the result of the expression?")
    result = test_game(generate_question, check_answer, name)
    if result:
        print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    main()
