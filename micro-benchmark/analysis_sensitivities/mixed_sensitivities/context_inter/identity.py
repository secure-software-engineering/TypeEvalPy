# A simple Python program that defines a function called 'identity' which calls another function 'uppercase' to perform conversion of the input string to uppercase.
# The given code is interprocedural because it involves calling a separate function ('uppercase') to complete the identity operation.
# Program is also context sensitive as it differ in context of function calls
def identity(x):
    if isinstance(x, str):
        result = uppercase(x)
    else:
        result = x
    return result


def uppercase(s):
    return s.upper()


a = identity(5)
b = identity("hello")
c = identity(2.5)
