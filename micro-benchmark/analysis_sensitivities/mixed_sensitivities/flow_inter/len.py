# A program that defines a function called `len_value` which returns the length of the input value.
# The function calls another function 'calculate_length' depending on the type of the input value.
# The behavior of the program is flow-sensitive as the function called depends on the flow of the program execution.


def len_value(value):
    if isinstance(value, str):
        return calculate_length(value)
    elif isinstance(value, list):
        return calculate_length(value)
    else:
        return None


def calculate_length(data):
    return len(data)


text = "Hello World"
numbers = [1, 2, 3, 4, 5]
result1 = len_value(text)
result2 = len_value(numbers)
