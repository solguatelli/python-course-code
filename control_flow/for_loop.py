print("--------------FOR LOOPS--------------")

# Iterate over objects
print("###For lists")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in nums:
    print(num)

for num in nums:
    if num % 2 == 0:
        print(num)

print("###For strings")
word = "Python"
for char in word:
    print(char)

print("###For tuples")
tup = (1, 2, 3)
for i in tup:
    print(i)

print("###Tuple unpacking")
pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]
for tuple in pairs:
    print(tuple)  # First way to show tuple values

for (a, b) in pairs:
    print(f"Tuple values: {a} and {b}")

for a, b in pairs:  # No need to use parenthesis
    print(f"Tuple values: {a} and {b}")

print("###For dictionaries")
d = {"k1": 1, "k2": 2, "k3": 4}
for item in d:
    print(item)  # By default, you iterate through the keys

for key, value in d.items():
    print(f"Key:{key} and value: {value}")

# When you don't plan on using the for loop variable:
print("###If you don't use the loop variable, use underscore")
for _ in (1, 2, 3):  # You use an underscore
    print("Placeholder")
