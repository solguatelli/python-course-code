print("--------------LOGICAL OPERATORS--------------")

a = 3
b = 8
c = -2

print(a > b and c < a)  # AND OPERATOR
print(a == b or c < b)  # OR OPERATOR
# Not operator, just like '!' in JavaScript, it returns the opposite boolean
print(not(1 == 1))

age = 16

if not(age > 18):
    print("You are still under aged")
# It's the same as this
if age < 18:
    print("You are still under aged")

