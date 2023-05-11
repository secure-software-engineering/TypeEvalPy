# A simple Python program that defines a function called 'arithmetic_op' which calls another function 'add' to perform addition of two integer parameters 'a' and 'b'.
# The given code is interprocedural because it involves calling a separate function ('add') to complete the arithmetic operation.
# Program is also flow sensitive as variable values changes over the execution flow.


def arithmetic_op(a, b):
    if a == 0:
        result = b
        return result
    elif b == 0:
        result = a
        return result
    else:
        result = add(a, b)

    if result < 0:
        result = None
    else:
        result = "Positive"
    return result


def add(a, b):
    result = a + b
    return result


x = 5
y = 10
result = arithmetic_op(x, y)
x = 0
result = arithmetic_op(x, y)
