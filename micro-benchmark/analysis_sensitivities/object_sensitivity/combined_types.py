# A class called CombinedTypesOperation is defined that takes one parameter my_bool in its constructor and has a method called my_function that returns either an integer or a string based on the value of my_bool.
# The class also has a member variable called result that stores the result of the computation.


class CombinedTypesOperation:
    def __init__(self, my_bool):
        self.my_bool = my_bool
        self.result = None

    def my_function(self):
        if self.my_bool:
            self.result = 5
        else:
            self.result = "Hello World!"
        return self.result


combined_op1 = CombinedTypesOperation(True)
combined_op2 = CombinedTypesOperation(False)
result1 = combined_op1.my_function()
result2 = combined_op2.my_function()
