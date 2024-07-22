# Class Variable is assigned to a variable
class MyClass:
    class_var = {'htdcm': 42, 'cxptu': 13, 'sebwa': 100}

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(76.27)
b = a.class_var
