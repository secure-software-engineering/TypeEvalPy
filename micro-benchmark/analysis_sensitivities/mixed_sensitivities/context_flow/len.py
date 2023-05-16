# A program that defines a function called 'compute_length' which returns the length of a string if it is a string, or the length of a list if it is a list.
# The behavior of the program is flow-sensitive as it produces different results based on the flow of execution.


def compute_length(s):
    if isinstance(s, str):
        return len(s)
    elif isinstance(s, list):
        return len(s)
    else:
        return None


text = "Hello World"
numbers = [1, 2, 3, 4, 5]
result1 = compute_length(text)
result2 = compute_length(numbers)
result3 = compute_length(10)
