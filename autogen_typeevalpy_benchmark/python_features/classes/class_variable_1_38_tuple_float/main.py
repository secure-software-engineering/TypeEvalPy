# Class Variable is assigned to a variable
class MyClass:
    class_var = (15, 56, 51)

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(55.34)
b = a.class_var
