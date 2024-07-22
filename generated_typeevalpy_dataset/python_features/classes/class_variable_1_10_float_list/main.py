# Class Variable is assigned to a variable
class MyClass:
    class_var = 42.33

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass([34, 11, 52])
b = a.class_var
