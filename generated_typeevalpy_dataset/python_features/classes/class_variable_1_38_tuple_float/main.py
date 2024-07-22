# Class Variable is assigned to a variable
class MyClass:
    class_var = (49, 5, 79)

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(97.53)
b = a.class_var
