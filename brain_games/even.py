import random
import prompt


def is_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in [1, 2, 3]:
        num = random.randrange(1, 100)
        print("Question: " + str(num))
        answer2 = prompt.string('Your answer: ')
        if (num % 2 == 0 and answer2 == "yes") or \
                (num % 2 == 1 and answer2 == "no"):
            print("Correct!")
        elif answer2 == "yes":
            print(answer2 + " is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, " + name + "!")
            break
        elif answer2 == "no":
            print(answer2 + " is wrong answer ;(. Correct answer was 'yes'.")
            print("Let's try again, " + name + "!")
            break
        elif answer2 != "yes" or answer2 != "no":
            print(answer2 + " is wrong answer ;(. Correct answer was 'yes'.")
            print("Let's try again, " + name + "!")
            break
    else:
        print("Congratulations, " + name)
