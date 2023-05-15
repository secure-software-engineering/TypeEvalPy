# A class called LengthOperation is defined that takes one parameter x in its constructor and has a method called compute_length that returns the length of the x attribute.
# The class also has a member variable called result that stores the result of the computation.


class Len:
    def __init__(self, x):
        self.x = x
        self.result = None

    def compute_length(self):
        self.result = len(self.x)
        return self.result


length_op1 = Len("Hello")
length_op2 = Len([1, 2, 3, 4, 5])
result1 = length_op1.compute_length()
result2 = length_op2.compute_length()
