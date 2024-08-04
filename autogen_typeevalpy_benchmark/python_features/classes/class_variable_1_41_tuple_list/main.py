# Class Variable is assigned to a variable
class MyClass:
    class_var = (65, 75, 92)

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass([56, 84, 18])
b = a.class_var
