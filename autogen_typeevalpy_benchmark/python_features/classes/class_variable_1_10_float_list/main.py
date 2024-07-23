# Class Variable is assigned to a variable
class MyClass:
    class_var = 65.56

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass([84, 84, 70])
b = a.class_var
