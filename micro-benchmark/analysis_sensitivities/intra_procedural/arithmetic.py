# This program is an example of intraprocedural analysis.
# The function arithmetic_op takes two integer parameters a and b, adds them together, and returns the result as a string indicating whether the result is "Positive" or "Negative" based on whether it is greater than or less than zero.
# The program does not call any other functions, so the analysis is focused on the behavior of this single function.
def arithmetic_op(a, b):
    result = a + b
    return result


result = arithmetic_op(5, -10)
