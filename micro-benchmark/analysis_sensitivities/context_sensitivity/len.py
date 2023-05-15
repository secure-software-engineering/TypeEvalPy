# Program defines a function called 'compute_length' which will simply return length of variable.
# The given code is context sensitive because it produces different results based on the context in which it is executed.


def compute_length(s):
    return len(s)


result = compute_length("Hello")
result = compute_length([5, 4, 3])
