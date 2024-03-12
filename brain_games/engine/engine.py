import prompt


def welcome_player():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def test_game(question_generator, check_answer, name, rounds=3):

    correct_answers = 0

    while correct_answers < rounds:
        question, correct_answer = question_generator()
        print('Question:', question)
        my_answer = input('Your answer: ')

        if check_answer(my_answer, correct_answer):
            print('Correct!')
            correct_answers += 1
        else:
            print(
                "'{}' is wrong answer ;(.\n"
                "Correct answer was '{}'.".format(my_answer, correct_answer)
            )
            print("Let's try again, {}!".format(name))
            return False

    return True
