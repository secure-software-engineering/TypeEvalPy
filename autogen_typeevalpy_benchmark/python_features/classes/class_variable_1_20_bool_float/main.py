# Class Variable is assigned to a variable
class MyClass:
    class_var = False

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(29.67)
b = a.class_var
