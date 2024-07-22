# Class Variable is assigned to a variable
class MyClass:
    class_var = (3, 35, 27)

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(47)
b = a.class_var
