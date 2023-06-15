# Program defines a class called IdentityOperation which takes one parameter x in its constructor, and has a method called identity that simply returns the x attribute. # The class also has a member variable called result that stores the result of the computation.


# This is object sensitive and the behavior of the identity method depends on the type of the x attribute of the instance.
class IdentityOperation:
    def __init__(self, x):
        self.x = x
        self.result = None

    def identity(self):
        if isinstance(self.x, str):
            return str(self.x)
        elif isinstance(self.x, int):
            return int(self.x)
        elif isinstance(self.x, float):
            return float(self.x)
        else:
            return self.x


identity_op = IdentityOperation(5)
result = identity_op.identity()

identity_op = IdentityOperation(1.0)
result = identity_op.identity()

identity_op = IdentityOperation("Hello World")
result = identity_op.identity()
