print("--------------WHILE LOOPS--------------")

x = 0
while x < 5:
    print(f"Value of x: {x}")
    x += 1

print("###You can also add an else statement")
x = 0
while x < 5:
    print(f"Value of x: {x}")
    x += 1
else:
    print("X is greater or equal than 5")

print("## Extra functionality with: break, continue and pass")

while True:
    print("Hello hello")
    if 3 > 2:
        break  # It interrupts the closest running loop

for i in (1, 2, 3):
    pass  # Does nothing, it's like a placeholder

for char in "Hello World":
    if char == " ":
        continue  # We stop current iteration and continue with the next, you go back to the top of the loop
        print("This doesn't get printed")
    print(char)

print("\n\n")
for char in "Hello World":
    if char == " ":
        break  # We stop the loop altogether
        print("This doesn't get printed")
    print(char)
