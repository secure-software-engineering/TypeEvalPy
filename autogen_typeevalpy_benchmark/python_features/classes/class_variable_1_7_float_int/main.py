# Class Variable is assigned to a variable
class MyClass:
    class_var = 62.7

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(89)
b = a.class_var
