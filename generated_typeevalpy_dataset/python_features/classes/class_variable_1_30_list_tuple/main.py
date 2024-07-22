# Class Variable is assigned to a variable
class MyClass:
    class_var = [12, 6, 90]

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass((41, 80, 76))
b = a.class_var
