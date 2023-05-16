# A program that defines a class called `MaxOperation` which takes two parameters `a` and `b` in its constructor and has a method called `find_max` which returns the maximum value between `a` and `b`.
# The behavior of the `find_max` method is object-sensitive as it depends on the type and value of the `a` and `b` attributes of the instance.


class MaxOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def find_max(self):
        if isinstance(self.a, int) and isinstance(self.b, int):
            return max(self.a, self.b)
        elif isinstance(self.a, float) and isinstance(self.b, float):
            return max(self.a, self.b)
        else:
            return None


max_op1 = MaxOperation(5, 10)
max_op2 = MaxOperation(3.5, 2)
result1 = max_op1.find_max()
result2 = max_op2.find_max()
