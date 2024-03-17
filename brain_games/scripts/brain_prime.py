#!/usr/bin/env python


from ..engine.engine import welcome_player, test_game
from ..games.brain_prime import get_number_and_prime_answer


def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def main():
    name = welcome_player()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    result = test_game(get_number_and_prime_answer, check_answer, name)

    if result:
        print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    main()
