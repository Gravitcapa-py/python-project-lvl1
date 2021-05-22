import random
import prompt


def progression(name):
    print('What number is missing in the progression?')
    for _ in [1, 2, 3]:
        position = random.randint(0, 9)
        start = random.randint(1, 4)
        step = random.randint(1, 5)
        i = 0
        base_list = [start]
        while i < 10:
            base_list.append(base_list[i] + step)
            i += 1
        result = base_list[position]
        base_list[position] = '..'
        print('Question:', end=' ')
        print(*base_list, sep=' ')
        answer = prompt.string('Your answer: ')
        base_list[position] = result
        if result == int(answer):
            print("Correct!")
        else:
            print("{} is wrong answer ;(. Correct answer was {}."
                  .format(answer, result))
            print("Let's try again, " + name + "!")
            break
    else:
        print("Congratulations, {}!".format(name))
