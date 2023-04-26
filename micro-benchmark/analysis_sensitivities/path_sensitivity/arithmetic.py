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
