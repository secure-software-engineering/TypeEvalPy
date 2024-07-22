# Class Variable is assigned to a variable
class MyClass:
    class_var = (35, 4, 38)

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass([14, 80, 16])
b = a.class_var
