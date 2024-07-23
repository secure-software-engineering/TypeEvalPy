# Class Variable is assigned to a variable
class MyClass:
    class_var = 93.49

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass((99, 38, 74))
b = a.class_var
