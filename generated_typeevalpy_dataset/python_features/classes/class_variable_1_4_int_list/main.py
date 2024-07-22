# Class Variable is assigned to a variable
class MyClass:
    class_var = 70

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass([13, 62, 98])
b = a.class_var
