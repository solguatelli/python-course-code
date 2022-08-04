print("----------I/O WITH BASIC FILES----------")

my_file = open('test.txt')
print(my_file.read())
my_file.seek(0)  # You move the cursor that reads the file to the start, otherwise you cant use .read again
# To get every new line separated:
text_lines = my_file.readlines()
print(text_lines)
my_file.close()  # To prevent errors

print("---Newer method to read/write")
with open("test.txt") as text_file:
    contents = text_file.read()

# No need to close the file manually
print(contents)

# OPEN METHOD : open(filename, mode = ...)
# mode = r // read only
# mode = w // write only (overwrites existing files or creates new ones)
# mode = a // append (like writing but you add to an existing file new lines, without overwriting)
# mode = r+ // read and write
# mode = w+ // write and read

with open("test.txt", mode="a") as f:
    f.write("\nA new line just added!!")

with open("new_file.txt", mode="w+") as f:
    f.write("I created this new file")
    print(f.read())
