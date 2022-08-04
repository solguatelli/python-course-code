print("----------------LIST COMPREHENSION----------------")

# A shorter way to express a for loop, use when we want to only fill arrays with values
# A beginner way

my_list = []
for i in range(5, 15):
    my_list.append(i)
print(my_list)

# A shorter way
my_list = [i for i in range(5, 15)]  # we have the variable and the source of the variable
print(my_list)

word = "morning"
chars = [char for char in word]
print(chars)

# It's also used for performing operations on each value of your source variable
print("Perform operations")
nums = [1, 2, 3, 4, 5]
nums_2 = [num * 2 for num in nums]
print(nums_2)

# You can also add conditions with if statements
even_nums = [x for x in range(15) if x % 2 == 0]
print(even_nums)

# You can add an 'else' statement too, but it may not look too easy to read sometimes
even_nums = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(even_nums)

# It also works for nested loops
result = []
for x in [2, 4, 6]:
    for y in [1, 10, 100]:
        result.append(x * y)
print(result)

# Shorter way, same result
result = [x * y for x in [2, 4, 6] for y in [1, 10, 100]]
print(result)
