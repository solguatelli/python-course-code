print("-----------LISTS-----------")
# Ordered sequences that can contain various datatypes
# Mutable

my_list = [1, 2, 3, 4, 5, 6]
my_list1 = ['one', 'two', 'three']
my_list2 = [1.23, 33, 100.455, True, 'Hello']

# Indexing and slicing
print("INDEXING AND SLICING")
print(my_list2[1:4])
print(my_list[2])

# Length and concatenation just like strings
print("LEN AND CONCATENATING")
print(len(my_list2))
print(my_list + my_list1)

# List are MUTABLE
print("LIST ARE MUTABLE")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
alphabet[0] = 'z'
alphabet[-2] = 'x'
print(alphabet)

# List methods
print("LIST METHODS")
print("---Push and pop---")
dogs = ["Miley", "Thor", "Fluffy"]
dogs.append("Ollie")
dogs.append("Junior")
popped_item = dogs.pop()
print(dogs)
# You can pop an element that's in any index
popped_item = dogs.pop(0)
print(popped_item)
print(dogs)
popped_item = dogs.pop(-1)
print(popped_item)
print(dogs)

# Sorting
print("---Sort method---")
nums = [1, 6, 10, 3, 2, 9]
print(nums)
nums.sort()
print(nums)

letters = ["b", "z", "ch", "c", "a", "h"]
print(letters)
letters.sort()
print(letters)

words = ["Sun", "Salty", "Sunny", "Apricot", "Jungle"]
print(words)
words.sort()
print(words)

# Reversing
print("---Reverse method---")
print(letters)
letters.reverse()
print(letters)
