# Class Variable is assigned to a variable
class MyClass:
    class_var = 54.61

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass('gueqc')
b = a.class_var
