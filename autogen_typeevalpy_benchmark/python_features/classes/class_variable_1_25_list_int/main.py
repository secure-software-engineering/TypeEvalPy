# Class Variable is assigned to a variable
class MyClass:
    class_var = [44, 23, 31]

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(8)
b = a.class_var
