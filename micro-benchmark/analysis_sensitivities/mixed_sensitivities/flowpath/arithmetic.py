# This program is path sensitive as depending on values of a and b execution path differs.
# It is also flow sensitive as variable value of x changes over the execution flow.


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


x = 5
y = 10
result = arithmetic_op(x, y)
x = 0
result = arithmetic_op(x, y)
