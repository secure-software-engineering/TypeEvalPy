# A Python program that defines a function called 'compute_length' which returns the length of the variable.
# The given code is flow-sensitive because it produces different results based on the flow of the program execution.


def compute_length(s):
    if isinstance(s, str):
        return len(s)
    elif isinstance(s, list):
        return len(s)
    else:
        return 1


result1 = compute_length("Hello")
result2 = compute_length([1, 2, 3, 4, 5])
result3 = compute_length(10)
