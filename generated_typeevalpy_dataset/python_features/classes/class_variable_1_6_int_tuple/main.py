# Class Variable is assigned to a variable
class MyClass:
    class_var = 41

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass((57, 31, 87))
b = a.class_var
