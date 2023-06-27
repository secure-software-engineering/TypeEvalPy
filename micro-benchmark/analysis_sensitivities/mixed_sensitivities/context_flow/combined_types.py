# A program that defines a function called 'process_data' which processes the input data based on its type.
# The behavior of the program is flow-sensitive as it produces different results based on the flow of execution.


def process_data(data):
    result = None
    if isinstance(data, int):
        result = data * 2
    elif isinstance(data, str):
        result = data * 5

    return result


result = process_data(5)
result = process_data("hello")
result = process_data(2.5)
