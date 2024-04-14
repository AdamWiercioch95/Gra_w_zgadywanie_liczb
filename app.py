
from random import randint


def random_number():
    return randint(1, 100)


def get_input():
    guess = input("Guess a number between 1 and 100: ")
    return guess


def validate_input(guess):
    while not guess.isdigit():
        print("It's not a number")
        guess = get_input()
    return int(guess)


def play():
    random_num = random_number()
    print(random_num)
    while True:
        guess = validate_input(get_input())
        if guess > random_num:
            print("Too big!")
        elif guess < random_num:
            print("Too small!")
        elif guess == random_num:
            return "You win!"


print(play())
