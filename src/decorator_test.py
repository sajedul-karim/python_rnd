import time
import functools

def operation_logger_decorator(original_function):
    @functools.wraps(original_function)
    def wrapper_function(*args, **kwargs):
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        start_time = time.time()
        result = original_function(*args, **kwargs)
        end_time = time.time()
        print(f"Result: {result}")
        print(f"Time taken: {end_time - start_time:.6f} seconds")
        return result
    return wrapper_function

@operation_logger_decorator
def calculator(a, b, operation='add'):
    """Perform basic arithmetic operations."""
    time.sleep(0.5)
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b if b != 0 else 'Error: Division by zero'
    else:
        return 'Error: Unknown operation'
    

operations = [
    ((1, 2), 'add'),
    ((1, 2), 'subtract'), 
    ((1, 2), 'multiply'),
    ((1, 2), 'divide'),
    ((1, 0), 'divide'),
    ((1, 2), 'unknown')
]

if __name__ == '__main__':
    for numbers, op in operations:
        calculator(*numbers, operation=op)
        print("\n\n")
