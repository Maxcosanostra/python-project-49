from brain_games.consts import AMOUNT_OF_ROUNDS
import prompt


def run_game(question_generator, instruction):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{instruction}')
    correct_answers = 0

    for _ in range(AMOUNT_OF_ROUNDS):
        question, correct_answer = question_generator()
        print('Question:', question)
        my_answer = prompt.string('Your answer: ')

        if my_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(
                f"'{my_answer}' is wrong answer ;(.\n"
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
