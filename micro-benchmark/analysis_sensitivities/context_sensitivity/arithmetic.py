# A simple Python program that defines a function called 'arithmetic_op'.
# The function takes two integer parameters 'a' and 'b', adds them together  and returns 0 if the result is greater than or equal to 5, or 'Negative' otherwise.
# The given code is context sensitive because it produces different results based on the context in which it is executed.


def arithmetic_op(a, b):
    result = a + b
    if result >= 5:
        result = 0
    else:
        result = "Negative"
    return result


x = 2
y = 1
result1 = arithmetic_op(x, y)
u = 3
v = 2
result2 = arithmetic_op(u, v)
