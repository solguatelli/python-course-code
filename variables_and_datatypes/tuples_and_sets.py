print("---------TUPLES---------")
# Ordered sequences of IMMUTABLE values
# Besides that they are pretty similar to lists

t = (1, 2, 3)
len(t)
type(t)
print(t[0])
print(t[-1])
print(t[1:])

# Methods : only two for tuples
print("--Tuple methods: index and count")
t = ('a', 'a', 'b', 'c')
print(t.count('a'))
print(t.index('a'))  # first appearance of the value

# t[0] = "NEW" --> will throw an error

print("---------SETS---------")
# Unordered collection of UNIQUE values
my_set = set()
my_set.add(1)
print(my_set)
my_set.add(3)
print(my_set)
my_set.add(1)  # Won't do anything because the value already exists
my_nums = [1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 2, 2, 2, 3]
print(set(my_nums))  # Great if you want to get rid of duplicates
