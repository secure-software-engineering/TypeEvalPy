# Class Variable is assigned to a variable
class MyClass:
    class_var = [89, 96, 40]

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(32.32)
b = a.class_var
