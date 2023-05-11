# This program is an example of flow sensitivity as the behavior of the program is dependent on the flow of execution, specifically the values assigned to the 'a' and 'b' fields of the 'arith_op' object.
# This program is an example of context sensitivity as the behavior of the program is dependent on the context of function call execution, specifically the values assigned to the 'a' and 'b' fields of the 'ArithmeticOperation' class objects.


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
