# Class Variable is assigned to a variable
class MyClass:
    class_var = [34, 90, 47]

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(13)
b = a.class_var
