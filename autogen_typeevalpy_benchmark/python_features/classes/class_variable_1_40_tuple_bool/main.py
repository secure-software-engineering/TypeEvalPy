# Class Variable is assigned to a variable
class MyClass:
    class_var = (81, 30, 37)

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(False)
b = a.class_var
