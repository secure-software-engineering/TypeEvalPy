# Program defines a class called MaxOperation which takes two parameters x and y in its constructor, and has a method called find_max that returns the maximum value between x and y.
# This program is object-sensitive and interprocedural as the behavior of the find_max method depends on the type and values of x and y attributes of the instance, and it calls the multiple function.


class MaxOperation:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.result = None

    def get_result(self):
        self.find_max()
        return self.result

    def find_max(self):
        self.result = max(self.x, self.y)


max_op1 = MaxOperation(5, 10)
max_op2 = MaxOperation(3.5, 2)
result1 = max_op1.get_result()
