import random
import prompt
import operator


def calc_gen(name):
    print('What is the result of expression?')
    for _ in [1, 2, 3]:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operations = {'+': operator.add,
                      '-': operator.sub,
                      '*': operator.mul}
        op = random.choice(list(operations.keys()))
        result = operations.get(op)(num1, num2)
        print("Question: {} {} {}".format(num1, op, num2))
        answer = prompt.string('Your answer: ')
        if result == float(answer):
            print("Correct!")
        else:
            print("{} is wrong answer ;(. Correct answer was {}."
                  .format(answer, result))
            print("Let's try again, " + name + "!")
            break
    else:
        print("Congratulations, " + name)
