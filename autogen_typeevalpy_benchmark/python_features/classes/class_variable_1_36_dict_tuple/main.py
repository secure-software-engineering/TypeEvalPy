# Class Variable is assigned to a variable
class MyClass:
    class_var = {'iixlk': 3, 'qtszr': 96, 'hlnxw': 54}

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass((80, 87, 90))
b = a.class_var
