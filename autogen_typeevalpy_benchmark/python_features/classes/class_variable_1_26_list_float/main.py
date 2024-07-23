# Class Variable is assigned to a variable
class MyClass:
    class_var = [12, 96, 67]

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(41.31)
b = a.class_var
