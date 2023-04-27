# A simple Python program that defines a function called 'arithmetic_op' which calls another function 'add' to perform addition of two integer parameters 'a' and 'b'.
# The given code is interprocedural because it involves calling a separate function ('add') to complete the arithmetic operation.
# Program is also flow sensitive as variable values changes over the execution flow.


def arithmetic_op(a, b):
    result = "Hello"
    result = add(a, b)
    return result


def add(a, b):
    result = a + b
    return result


result = arithmetic_op(5, 10)
