# Class Variable is assigned to a variable
class MyClass:
    class_var = {'qbkwz': 63, 'apftz': 41, 'wflse': 66}

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(55)
b = a.class_var
