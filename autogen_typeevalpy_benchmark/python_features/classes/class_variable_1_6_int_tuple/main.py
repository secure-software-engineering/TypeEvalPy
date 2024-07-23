# Class Variable is assigned to a variable
class MyClass:
    class_var = 21

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass((10, 29, 46))
b = a.class_var
