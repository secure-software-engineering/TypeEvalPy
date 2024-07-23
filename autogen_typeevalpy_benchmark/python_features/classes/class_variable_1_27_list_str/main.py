# Class Variable is assigned to a variable
class MyClass:
    class_var = [40, 100, 90]

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass('wjyoc')
b = a.class_var
