# Class Variable is assigned to a variable
class MyClass:
    class_var = [92, 83, 88]

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass((66, 47, 25))
b = a.class_var
