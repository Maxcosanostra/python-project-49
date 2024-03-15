#!/usr/bin/env python


from ..engine.engine import welcome_player, test_game
from ..games.brain_calc import get_math_expression_and_result


def check_answer(my_answer, correct_answer):
    return my_answer == correct_answer


def main():
    name = welcome_player()
    print("What is the result of the expression?")
    result = test_game(get_math_expression_and_result, check_answer, name)
    if result:
        print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    main()
