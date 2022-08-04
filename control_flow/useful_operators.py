print("--------------USEFUL OPERATORS--------------")

print("-----The 'range' function")
# It's a generator of numbers
for i in range(5):  # One arg: stop argument, from 0 up to but not including
    print(i)

print("\n\n")
for i in range(2, 10, 2):
    print(i)

# If you want to save the information generated you cast it as a list
print("---Cast range as list")
generated_list = list(range(2, 10, 2))
print(generated_list)

print("-----The 'enumerate' function")
# We sometimes need the index of the object we are iterating
# The first option could be:

index_count = 0
word = "hello"
for char in word:
    print(f"The letter at index {index_count} is {char}")
    index_count += 1

print("\n")
# Python has a built-in function that gives you index-value tuples so there is no need to save the index
for index, char in enumerate(word):
    print(f"The letter at index {index} is {char}")

print("\n")
print("-----The 'zip' function")
# Opposite to the other methods, it zips in tuples multiple lists

list1 = [1, 2, 3]  # if one lists has more values it works the same, with the minimun amount both lists have
list2 = ["a", "b", "c"]
for item in zip(list1, list2):
    print(item)

print("\n")
print("-----The 'in' keyword")
# To quickly check if a value is a part of an object
print("d" in "abc")
print(1 in [1, 2, 3])
print("key1" in {"key1": 1, "key2": 2})
print(2 in {"key1": 1, "key2": 2}.values())

print("\n")
print("-----The min and max functions")
numbers = [96, 2, 30, 4, 100, -2]
print(max(numbers))
print(min(numbers))

print("\n")
print("-----The random library")
# We first import the library to our code
# Shuffle function
from random import shuffle

new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(new_list)
print("Shuffled list")
shuffle(new_list)
print(new_list)

### Randint function
from random import randint

print("Random integers:")
rand_number = randint(0, 10)
print(rand_number)

print("\n")
print("-----User input")
# Always saved as a string

user_input = input("Give me a number: ")
print(user_input)

# We need to cast number inputs
result = float(user_input) + 30
