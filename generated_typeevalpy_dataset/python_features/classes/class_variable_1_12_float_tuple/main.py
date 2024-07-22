# Class Variable is assigned to a variable
class MyClass:
    class_var = 11.81

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass((25, 79, 17))
b = a.class_var
