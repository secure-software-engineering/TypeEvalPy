# A program that defines a function called 'process_data' which processes the input data based on its type.
# The behavior of the program is interprocedural as it involves calling a separate function ('double_value' and 'uppercase') to process the data.
# The program is also context-sensitive as the behavior of the 'double_value' and 'uppercase' functions depend on the type of the input.


def process_data(data):
    if isinstance(data, int):
        result = double_value(data)
    elif isinstance(data, str):
        result = double_value(data)
    else:
        result = None
    return result


def double_value(num):
    return num * 2


value1 = 5
value2 = "hello"
value3 = 2.5
result1 = process_data(value1)
result2 = process_data(value2)
result3 = process_data(value3)
