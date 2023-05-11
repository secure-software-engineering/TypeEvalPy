# A simple Python program that defines a function called 'arithmetic_op' which calls another function 'add' to perform addition of two integer parameters 'a' and 'b'.
# The given code is interprocedural because it involves calling a separate function ('add') to complete the arithmetic operation.
# Program is also context sensitive as it differ in context of function calls


def arithmetic_op(a, b):
    result = add(a, b)
    return result


def add(a, b):
    result = a + b
    return result


x = 2
y = 1
result1 = arithmetic_op(x, y)
u = 3
v = 2
result2 = arithmetic_op(u, v)
