# Class Variable is assigned to a variable
class MyClass:
    class_var = {'guemp': 42, 'llqtz': 61, 'lkuyj': 17}

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass((16, 68, 30))
b = a.class_var
