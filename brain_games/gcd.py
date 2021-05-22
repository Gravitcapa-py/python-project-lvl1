import random
import prompt
from math import gcd


def gcd_f(name):
    print('Find the greatest common divisor of given numbers')
    for _ in [1, 2, 3]:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        result = gcd(num1, num2)
        print("Question: {} {} ".format(num1, num2))
        answer = prompt.string('Your answer: ')
        if result == int(answer):
            print("Correct!")
        else:
            print("{} is wrong answer ;(. Correct answer was {}.".format(answer, result))
            print("Let's try again, " + name + "!")
            break
    else:
        print("Congratulations, " + name)
