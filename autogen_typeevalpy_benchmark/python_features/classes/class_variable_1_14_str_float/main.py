# Class Variable is assigned to a variable
class MyClass:
    class_var = 'xuvaf'

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(61.58)
b = a.class_var
