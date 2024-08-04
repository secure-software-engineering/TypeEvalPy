# Class Variable is assigned to a variable
class MyClass:
    class_var = False

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass([5, 46, 65])
b = a.class_var
