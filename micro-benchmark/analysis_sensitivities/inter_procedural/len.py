# A program that defines a function called 'compute_length' which returns the length of the input variable.
# The function is called from another function 'operation' which takes two parameters and returns the sum of their lengths.


def compute_length(s):
    return len(s)


def operation(a, b):
    result = compute_length(a) + compute_length(b)
    return result


result = operation("Hello", "World")
