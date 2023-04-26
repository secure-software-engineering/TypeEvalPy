# This program is an example of path-sensitivity as it considers different possible execution paths based on the input values of 'a' and 'b'.
# If either 'a' or 'b' is zero, the program will take a different execution path and return the non-zero value as the result.
# Otherwise, the program will add 'a' and 'b' together and return the sum as the result.
# The result is then checked for positivity or negativity and returned accordingly.


def arithmetic_op(a, b):
    if a == 0:
        result = b
    elif b == 0:
        result = a
    else:
        result = a + b

    if result < 0:
        result = "Negative"
    else:
        result = "Positive"
    return result


result = arithmetic_op(5, 10)
