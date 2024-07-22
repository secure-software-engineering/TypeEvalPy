# Class Variable is assigned to a variable
class MyClass:
    class_var = {'enygk': 91, 'ljiaj': 20, 'ygwfy': 33}

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass('snppo')
b = a.class_var
