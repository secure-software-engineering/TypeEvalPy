# Class Variable is assigned to a variable
class MyClass:
    class_var = 30

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass({'qshvt': 68, 'gozoh': 29, 'foiom': 19})
b = a.class_var
