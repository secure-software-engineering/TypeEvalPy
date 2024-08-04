# Class Variable is assigned to a variable
class MyClass:
    class_var = [58, 46, 98]

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass('elhur')
b = a.class_var
