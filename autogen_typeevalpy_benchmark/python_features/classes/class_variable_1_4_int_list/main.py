# Class Variable is assigned to a variable
class MyClass:
    class_var = 58

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass([32, 56, 44])
b = a.class_var
