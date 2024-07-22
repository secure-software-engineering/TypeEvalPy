# Class Variable is assigned to a variable
class MyClass:
    class_var = 55

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass('vylqk')
b = a.class_var
