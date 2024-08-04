# Class Variable is assigned to a variable
class MyClass:
    class_var = (12, 25, 19)

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass({'uubkw': 23, 'knkyf': 27, 'lbrvy': 3})
b = a.class_var
