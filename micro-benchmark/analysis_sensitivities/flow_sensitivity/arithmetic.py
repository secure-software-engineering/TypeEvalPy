# A simple Python program that defines a function called 'arithmetic_op'.
# The function takes two integer parameters 'a' and 'b', adds them together and checks if the result is positive or negative.
# The code is flow-sensitive because it changes its type of 'result' based on the flow of the program execution.


def arithmetic_op(a, b):
    result = a + b

    if result < 0:
        result = "Negative"
    else:
        result = "Positive"
    return result


result = arithmetic_op(5, 10)
