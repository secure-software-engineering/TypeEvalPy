# Class Variable is assigned to a variable
class MyClass:
    class_var = [8, 30, 67]

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(True)
b = a.class_var
