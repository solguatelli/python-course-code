print("--------------FUNCTIONS--------------")


# Structure of a simple function
def name_of_function(parameter):
    """
    Optional docstring that explains the function
    :param parameter: param_name
    :return: none
    """
    pass


def say_hello(name):
    print(f"Hello {name}!")


say_hello("Sol")


# say_hello()  --> An error occurs because the parameters is mandatory, if you want optional params:
def say_hello(name="No name"):
    print(f"Hello {name}")


say_hello()


# If we want to save a value calculated in a function, we use a RETURN keyword
def my_sum(num1, num2):
    return num1 + num2


result = my_sum(2, 3)
print(result)


def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
    return False


def get_even_numbers(num_list):
    even_nums = []
    for num in num_list:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums


print(check_even_list([1, 2, 3]))
print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

### Tuple unpacking in functions
work_hours = [("Abby", 20), ("Cassie", 30), ("John", 50)]


def get_best_employee(employee_details):
    current_max = 0
    employee_of_month = ""

    for employee, hour in employee_details:
        if hour > current_max:
            current_max = hour
            employee_of_month = employee
        else:
            pass
    return current_max, employee_of_month


# result = get_best_employee(work_hours)
a, b = get_best_employee(work_hours)
print(f"The best employee of the month was {b}")
print(f"He worked {a} hours!")

print("----*ARGS - *KWARGS----")

print("*args and **kwargs")


# -----------------  Functional parameters *args and *kwargs (keyword arguments)
# They let us take an arbitrary number of arguments, like the rest operator in JS
# *args saves all arguments in a tuple - it can be any name as long as you have the star in front (*things)

def my_function(*args):
    print(args)
    return sum(args) * 0.05


print(my_function(40, 50, 10, 12))


# **kwargs saves named arguments in a dictionary - the key is the parameter name and the value is the parameter value
# - it can be any name as long as you have the two stars in front (**jelly)

def my_other_function(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print(f"Mi favorite fruit is {kwargs['fruit']}")
    else:
        print("No favorite fruit found!")


my_other_function(fruit='apple', veggie='carrot')


def mixed_function(*args, **kwargs):
    print(args)
    print(kwargs)


mixed_function(1, 2, 3, 4, fruit='orange', veggie='tomato')

# respect the order of the parameters when you pass it to the function

print("# Lambda expressions")


# --------------- Lambda expressions: like anonymous functions in JavaScript you use it once, and they don't have a name

# Let's first see the built-in functions MAP and FILTER
# MAP
def square(num):
    return num * num


for item in map(square, [1, 2, 3, 4, 5]):
    print(item)

result_arr = list(map(square, [1, 2, 3, 4, 5]))
print(result_arr)


def even_len(name):
    if len(name) % 2 == 0:
        return "EVEN"
    else:
        return name[0]


for item in map(even_len, ["Ana", "Samy", "Collin"]):
    print(item)


# Filter
# Just like filter in Javascript, you only return the items that returned True when mapped to the function


def check_even_num(num):
    return num % 2 == 0


for item in filter(check_even_num, [1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print(item)

even_nums = list(filter(check_even_num, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# Lambda expressions
# First, a regular function

def double(num):
    return num * 2


# Now the lambda simplification
# lambda num: num * 2

# We use it in conjunction with other functions just like map and filter
double_nums = list(map(lambda num: num * 2, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(double_nums)

print("# Scope")

# LEGB RULE for scope: order that Python uses to search for variables
# LOCAL: inside a function (def or lambda)
# ENCLOSING FUNCTION LOCALS : from inner to outer functions
# GLOBAL
# BUILT-IN

# Global
name = "Austin"


def greet():
    # Enclosing
    name = "Bella"

    def hello():
        # Local
        name = "Chloe"
        print("Hello " + name)

    hello()


greet()

# Global keyword
# We can reach for global variables and change their value inside a function

x = 50


def func():
    global x  # we will explicitly use the global x
    print(x)
    x = "Hello new value here"
    print("Just changed global X to: " + x)


func()
print(x)


# Much better to take parameter and return a new value, much safer

def func_regular(x):
    print(x)
    x = "Hello new value here"
    print("Just changed local X to: " + x)
    return x


# Much clearer reassignment
x = func_regular(x)
print(x)
