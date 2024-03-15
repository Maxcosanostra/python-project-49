#!/usr/bin/env python

from .. engine.engine import welcome_player, test_game
from .. games.brain_gcd import get_nums_pair_and_gcd


def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def main():
    name = welcome_player()
    print("Find the greatest common divisor of given numbers.")

    result = test_game(get_nums_pair_and_gcd, check_answer, name)

    if result:
        print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    main()
