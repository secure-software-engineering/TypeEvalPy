# This program is an example of context and object sensitivity as it uses an object to store the input values and the computed result.
# The behavior of the program depends on the context object passed to the 'arithmetic_op' function, which contains the input values 'a' and 'b', as well as the computed result.
# The 'result' field is accessed and modified in a context-sensitive manner, where the behavior of the program depends on the specific context object that is used.
class CallContext:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = None


def arithmetic_op(context):
    result = context.a + context.b
    context.result = result


context1 = CallContext(2, 1)
arithmetic_op(context1)
result1 = context1.result

context2 = CallContext("Hello", "World")
arithmetic_op(context2)
result2 = context2.result
