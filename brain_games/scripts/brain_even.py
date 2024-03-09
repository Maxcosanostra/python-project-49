import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def is_even(number):
    return number % 2 == 0


def get_number_and_even_answer():
    number = random.randint(1, 100)
    result = 'yes' if is_even(number) else 'no'
    return number, result


def test_even_game(name):
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    correct_answers_in_row = 0

    while correct_answers_in_row < 3:
        number, system_answer = get_number_and_even_answer()
        print('Question: ', number)
        my_answer = input()

        if my_answer == system_answer:
            print('Correct!')
            correct_answers_in_row += 1
        else:
            print(
                "'yes' is wrong answer ;(. Correct answer was 'no'.\n"
                "Let's try again, {}!".format(name)
            )
            correct_answers_in_row = 0

    print("Congratulations, {}!".format(name))


name = welcome_user()
test_even_game(name)
