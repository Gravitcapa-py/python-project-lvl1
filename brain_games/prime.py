import random
import prompt


def prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in [1, 2, 3]:
        number = random.randint(2, 9)
        d = 2
        while number % d != 0:
            d += 1
        result = "yes" if d == number else "no"
        print('Question: {}'.format(number))
        answer = prompt.string('Your answer: ')

        if result == answer:
            print("Correct!")
        else:
            print("{} is wrong answer ;(. Correct answer was {}."
                  .format(answer, result))
            print("Let's try again, " + name + "!")
            break
    else:
        print("Congratulations, {}!".format(name))
