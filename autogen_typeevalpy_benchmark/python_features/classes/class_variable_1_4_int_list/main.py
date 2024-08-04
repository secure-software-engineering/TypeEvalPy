# Class Variable is assigned to a variable
class MyClass:
    class_var = 51

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass([57, 98, 91])
b = a.class_var
