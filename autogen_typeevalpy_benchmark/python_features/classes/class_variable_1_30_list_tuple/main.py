# Class Variable is assigned to a variable
class MyClass:
    class_var = [55, 37, 95]

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass((54, 64, 5))
b = a.class_var
