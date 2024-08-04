# Class Variable is assigned to a variable
class MyClass:
    class_var = 30.09

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(85)
b = a.class_var
