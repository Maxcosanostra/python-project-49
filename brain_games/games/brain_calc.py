import random
import operator


OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_math_expression_and_result():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(list(OPERATORS.keys()))
    question = f"{num1} {operator} {num2}"
    correct_answer = str(OPERATORS[operator](num1, num2))
    return question, correct_answer
