# A simple Python program that defines a function called 'arithmetic_op' which calls another function 'add' to perform addition of two integer parameters 'a' and 'b'.
# The 'add' function takes two integer parameters 'a' and 'b', adds them together, and returns the result.
# The given code is interprocedural because it involves calling a separate function ('add') to complete the arithmetic operation.


def add(a, b):
    result = a + b
    return result


def arithmetic_op(a, b):
    result = add(a, b)
    return result

result = arithmetic_op(<value1>, <value1>)
