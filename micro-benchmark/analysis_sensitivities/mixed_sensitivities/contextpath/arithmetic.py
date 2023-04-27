# This program is an example of path-sensitivity and context sensitivity it considers different possible execution paths based on the context that is input values of 'a' and 'b'.
# If either 'a' or 'b' is zero, the program will take a different execution path and return the non-zero value as the result.
# Otherwise, the program will add 'a' and 'b' together and store the sum as the result.
# The result is then checked for positivity and returned.


def arithmetic_op(a, b):
    if a == 0:
        result = b
        return result
    elif b == 0:
        result = a
        return result
    else:
        result = a + b

    if result < 0:
        result = None
    else:
        result = "Positive"
    return result


result = arithmetic_op(5, 10)
result2 = arithmetic_op(0, 10)
result2 = arithmetic_op(-5, -10)
