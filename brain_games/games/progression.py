import random
from brain_games.engine import run_game
from brain_games.consts import PROGRESSION_INSTRUCTION
from brain_games.consts import SHORT_PROGR_LENGHT, LONG_PROGR_LENGHT


def get_progression_and_missed_number():
    progression_length = random.randint(SHORT_PROGR_LENGHT, LONG_PROGR_LENGHT)

    start = random.randint(1, 100)
    step = random.randint(1, 100)

    progression = [start + step * i for i in range(progression_length)]
    missed_index = random.randint(0, progression_length - 1)
    missed_number = progression[missed_index]
    progression[missed_index] = '..'
    progression_with_missed_number = ' '.join(map(str, progression))

    return progression_with_missed_number, str(missed_number)


def run_progression_game():
    run_game(get_progression_and_missed_number, PROGRESSION_INSTRUCTION)
