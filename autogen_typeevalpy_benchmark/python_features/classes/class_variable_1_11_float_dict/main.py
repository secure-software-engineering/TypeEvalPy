# Class Variable is assigned to a variable
class MyClass:
    class_var = 97.65

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass({'vsujg': 9, 'lpzhh': 74, 'lmeuq': 44})
b = a.class_var
