# Class Variable is assigned to a variable
class MyClass:
    class_var = (47, 57, 13)

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(False)
b = a.class_var
