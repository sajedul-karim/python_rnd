from functools import reduce

def pipe(value, *functions):
    return reduce(lambda acc, func: func(acc), functions, value)

# Define the functions
def square(num):
    return num ** 2

def add_one(num):
    return num + 1

# Use the pipe function
result = pipe(5, square, add_one)
print(result)  # Output: 26
