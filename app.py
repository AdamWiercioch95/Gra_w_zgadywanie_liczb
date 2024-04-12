# Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 – 100. Następnie:
#
# Zadać pytanie: "Guess the number: " i pobrać liczbę z klawiatury.
# Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat "It's not a number!", po czym wrócić do pkt. 1
# Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat "Too small!", po czym wrócić do pkt. 1.
# Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić komunikat "Too big!", po czym wrócić do pkt. 1.
# Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat "You win!", po czym zakończyć działanie programu.
# Przykład:
# Guess the number: cześć
# It's not a number!
# Guess the number: 50
# Too small!
# Guess the number: 75
# Too big!
# Guess the number: 63
# You win!
#
# Pamiętaj, aby obsłużyć odpowiednie błędy!
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
