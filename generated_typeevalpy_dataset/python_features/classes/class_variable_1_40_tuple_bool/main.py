# Class Variable is assigned to a variable
class MyClass:
    class_var = (68, 66, 73)

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(False)
b = a.class_var
