# Program defines a class called IdentityOperation which takes one parameter x in its constructor, and has a method called identity that simply returns the x attribute.
# The class also has a member variable called result that stores the result of the computation.

# This is object sensitive and the behavior of the identity method depends on the type of the x attribute of the instance.
# The 'result' field is accessed and modified in a context-sensitive manner, where the behavior of the program depends on the specific context object that is used.


class IdentityOperation:
    def __init__(self, x):
        self.x = x
        self.result = None


def identity(context):
    context.result = context.x
    return type(context.result)


context1 = IdentityOperation(5)
context2 = IdentityOperation("Hello World")
result1 = identity(context1)
result2 = identity(context2)
