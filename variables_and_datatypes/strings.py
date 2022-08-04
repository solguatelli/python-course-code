print("-----Strings - sequence of characters-----")
print("# Ordered and immutable")

my_name = 'Sol'
my_pets = "Sunny and Moonshine"
alphabet = "abcdefghijk"
print(type(my_name))

# Escape sequences
print("She said to me: \"You are crazy!\"")
print("n for \nnew line")
print("t for \ttab")
print("\\")

# Indexing - single character
print(my_pets[0])
print(my_pets[-1])
print(my_pets[-4])
# Slicing - slice of string [start:stop:step]
print(my_pets[0:5])
print(my_pets[:5])
print(my_pets[10:])
print(my_pets[6:10])
print(my_pets[:])
# With steps
print(alphabet[::2])

# TRICK TO REVERSE A STRING
print(alphabet[::-1])

# Length of a string
print(len(alphabet))

# Built-in methods
x = "Hello World"
print(x.upper())
print(x.lower())
print(x.split())
print(x.split('o'))

# Concatenating
print("The first letters of the alphabet are " + alphabet)
letter = "z"
print(letter * 10)

# Formatting
# 1. .format()
print("This is a {} inserted".format("string"))
print("The {2} {1} {0}".format("fox", "brown", "quick"))
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))

# 1.1 Float formatting {value:width.precision} width: length of resulting string, precision: number of decimals
result = 100 / 777
print(result)
print("The result is {r:1.3f}".format(r=result))

# 2. f-strings
name = "Jose"
age = 21
print(f"Hello I'm {name} and I'm {age} years old")
