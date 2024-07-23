# Class Variable is assigned to a variable
class MyClass:
    class_var = 65

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(69.84)
b = a.class_var
