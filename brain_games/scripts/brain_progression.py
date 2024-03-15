#!/usr/bin/env python


from ..engine.engine import welcome_player, test_game
from ..games.brain_progression import get_progression_and_missed_number


def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def main():
    name = welcome_player()
    print("What number is missing in the progression?")

    result = test_game(get_progression_and_missed_number, check_answer, name)

    if result:
        print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    main()
