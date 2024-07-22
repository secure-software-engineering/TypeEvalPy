# Class Variable is assigned to a variable
class MyClass:
    class_var = [90, 60, 37]

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(37.27)
b = a.class_var
