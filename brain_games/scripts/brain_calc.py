#!/usr/bin/env python3
from brain_games.calc import calc_gen
from brain_games import cli


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    calc_gen(name)


if __name__ == '__main__':
    main()
