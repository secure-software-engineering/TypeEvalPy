# A class called CombinedTypes is defined. The class includes a method called my_function that has a combined return type [int, str].
# This is field-sensitive, allowing the value member variable to store different types of values


class CombinedTypes:
    def __init__(self, x):
        self.value = x

    def my_function(self):
        if self.value:
            x = 5
        else:
            x = "Hello World!"
        return x


combined = CombinedTypes(5)
combined.value = False
result = combined.my_function()
