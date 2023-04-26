# The program is an example of context and flow sensitivity.
# The function arithmetic_op takes two integer parameters a and b, and adds them together.
# If the result is greater than or equal to 5, it returns 0, otherwise it returns the string "Negative".
# The output of the function depends on the input values and the control flow within the function, making it context and flow sensitive.


def arithmetic_op(a, b):
    result = a + b
    if result >= 5:
        return 0
    else:
        return "Negative"


output1 = arithmetic_op(2, 1)
output2 = arithmetic_op(4, 2)
