#!/usr/bin/env python3
from brain_games.scripts.brain_even import is_even
from brain_games import cli


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    is_even(name)


if __name__ == '__main__':
    main()
