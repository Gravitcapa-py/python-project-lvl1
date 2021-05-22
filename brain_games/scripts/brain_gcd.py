#!/usr/bin/env python3
from brain_games.gcd import gcd_f
from brain_games import cli


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    gcd_f(name)


if __name__ == '__main__':
    main()
