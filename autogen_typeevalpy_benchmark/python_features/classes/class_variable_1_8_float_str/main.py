# Class Variable is assigned to a variable
class MyClass:
    class_var = 21.1

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass('iudvd')
b = a.class_var
