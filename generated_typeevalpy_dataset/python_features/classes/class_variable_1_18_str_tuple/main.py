# Class Variable is assigned to a variable
class MyClass:
    class_var = 'ipgys'

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass((75, 23, 87))
b = a.class_var
