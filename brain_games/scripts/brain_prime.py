#!/usr/bin/env python3
from brain_games.prime import prime
from brain_games import cli


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    prime(name)


if __name__ == '__main__':
    main()
