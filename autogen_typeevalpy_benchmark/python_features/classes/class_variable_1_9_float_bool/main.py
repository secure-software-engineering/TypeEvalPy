# Class Variable is assigned to a variable
class MyClass:
    class_var = 96.68

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(True)
b = a.class_var
