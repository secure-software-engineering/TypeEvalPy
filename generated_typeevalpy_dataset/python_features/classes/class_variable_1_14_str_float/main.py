# Class Variable is assigned to a variable
class MyClass:
    class_var = 'rodyt'

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(23.73)
b = a.class_var
