# Class Variable is assigned to a variable
class MyClass:
    class_var = 'pmzic'

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass([82, 55, 82])
b = a.class_var