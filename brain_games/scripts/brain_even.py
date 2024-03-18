#!/usr/bin/env python


from ..engine.engine import welcome_player, test_game
from ..games.brain_even import get_number_and_even_answer


def check_answer(my_answer, correct_answer):
    return my_answer == correct_answer


def main():
    name = welcome_player()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    result = test_game(get_number_and_even_answer, check_answer, name)
    if result:
        print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    main()
