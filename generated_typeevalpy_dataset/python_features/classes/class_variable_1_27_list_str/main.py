# Class Variable is assigned to a variable
class MyClass:
    class_var = [99, 81, 23]

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass('vryiw')
b = a.class_var
