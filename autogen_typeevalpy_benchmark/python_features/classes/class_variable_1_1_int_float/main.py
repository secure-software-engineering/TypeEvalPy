# Class Variable is assigned to a variable
class MyClass:
    class_var = 10

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(91.72)
b = a.class_var
