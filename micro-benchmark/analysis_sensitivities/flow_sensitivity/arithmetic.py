# A simple Python program that defines a function called 'arithmetic_op'.
# The function takes two integer parameters 'a' and 'b', adds them together and returns.
# The code is flow-sensitive because it changes its type of 'result' based on the flow of the program execution.


def arithmetic_op(a, b):
    result = a + b
    if result >= 5:
        return result
    else:
        return "Negative"


x = 2
y = 1
result = arithmetic_op(x, y)

u = 3
v = 2
result = arithmetic_op(u, v)
