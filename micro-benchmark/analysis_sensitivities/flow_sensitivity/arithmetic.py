def arithmetic_op(a, b):
    result = a + b

    if result < 0:
        result = "Negative"
    else:
        result = "Positive"
    return result


result = arithmetic_op(5, 10)
