# Class Variable is assigned to a variable
class MyClass:
    class_var = 39.53

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass((56, 5, 81))
b = a.class_var
