# A simple Python program that defines a function called 'arithmetic_op'.
# The function takes two integer parameters 'a' and 'b', adds them together  and returns result.
# The given code is context sensitive because it produces different results based on the context in which it is executed.


def arithmetic_op(a, b):
    result = a + b
    return result


result1 = arithmetic_op(5, 10)
result2 = arithmetic_op(5.2, 10.3)
result3 = arithmetic_op("Hello", "World")
