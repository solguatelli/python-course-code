from random import shuffle

game_list = [' ', 'O', ' ']


def shuffle_list(data_list):
    shuffle(data_list)
    return data_list


def player_guess():
    guess = ''

    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0, 1 or 2 for position: ")
    return int(guess)


def check_guess(my_list, user_guess):
    if my_list.index("O") == user_guess:
        print("You won!")
    else:
        print(f"Wrong guess {my_list}")


#########

mixed_list = shuffle_list(game_list)

guess = player_guess()

check_guess(mixed_list, guess)
