# Class Variable is assigned to a variable
class MyClass:
    class_var = 14

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass((26, 2, 45))
b = a.class_var
