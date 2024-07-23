# Class Variable is assigned to a variable
class MyClass:
    class_var = {'jvifq': 89, 'gfktm': 51, 'oeniu': 82}

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(54)
b = a.class_var
