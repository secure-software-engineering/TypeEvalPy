# The given code is an example of field sensitivity because it can recognize values based on the values assigned to its member variables.
# It also demonstrates multiple levels of field sensitivity.


class CombinedTypes:
    def __init__(self, my_bool):
        self.value = self.Value()
        self.value.my_bool = my_bool

    class Value:
        def __init__(self):
            self.my_bool = False

        def my_function(self):
            if self.my_bool:
                x = 5
            else:
                x = "Hello World!"
            return x

    def my_function(self):
        return self.value.my_function()


combined = CombinedTypes(5)
combined.value.my_bool = True
result1 = combined.my_function()

combined.value.my_bool = False
result2 = combined.my_function()
