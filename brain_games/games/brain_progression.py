import random


def get_progression_and_missed_number():
    progression_length = random.randint(5, 10)

    start = random.randint(1, 100)
    step = random.randint(1, 100)

    progression = [start + step * i for i in range(progression_length)]
    missed_index = random.randint(0, progression_length - 1)
    missed_number = progression[missed_index]
    progression[missed_index] = '..'
    progression_with_missed_number = ' '.join(map(str, progression))

    return progression_with_missed_number, str(missed_number)
