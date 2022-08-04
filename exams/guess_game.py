from random import randint

num = randint(1, 101)
print(num)
guesses = []

while True:
    user_input = int(input("Guess the number between 1 and 100: "))
    guesses.append(user_input)
    if user_input == num:
        break

    if len(guesses) == 1:
        if user_input in list(range(num - 10, num + 11)):
            print(user_input)
            print("WARM!")
        else:
            print(user_input)
            print("COLD!")
    else:
        if abs(num - guesses[-1]) < abs(num - guesses[-2]):
            print(user_input)
            print("WARMER!")
        else:
            print(user_input)
            print("COLDER!")

print(f"You guessed correctly! In only {len(guesses)} guesses")
