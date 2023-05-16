# A program that defines a function called 'process_data' which processes the input data based on its type.
# The behavior of the program is flow-sensitive as it produces different results based on the flow of execution.


def process_data(data):
    if isinstance(data, int):
        return data * 2
    elif isinstance(data, str):
        return data.upper()
    else:
        return None


result1 = process_data(5)
result2 = process_data("hello")
result3 = process_data(2.5)
