# Program defines a class called IdentityOperation which takes one parameter x in its constructor, and has a method called identity that simply returns the x attribute. # The class also has a member variable called result that stores the result of the computation.
# This is object and inter procedural sensitive and the behavior of the identity method depends on the type of the x attribute of the instance and it calls another function ' operation'


class IdentityOperation:
    def __init__(self, x):
        self.x = x
        self.result = None

    def identity(self):
        self.result = self.operation()
        return self.result

    def operation(self):
        self.result = type(self.x)
        return self.result


identity_op1 = IdentityOperation(5)
identity_op2 = IdentityOperation("Hello World")
result1 = identity_op1.identity()
result2 = identity_op2.identity()
