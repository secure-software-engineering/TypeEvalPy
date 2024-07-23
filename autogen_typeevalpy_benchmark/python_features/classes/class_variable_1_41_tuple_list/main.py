# Class Variable is assigned to a variable
class MyClass:
    class_var = (97, 56, 39)

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass([14, 14, 42])
b = a.class_var
