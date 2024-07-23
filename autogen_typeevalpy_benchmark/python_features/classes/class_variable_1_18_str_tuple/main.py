# Class Variable is assigned to a variable
class MyClass:
    class_var = 'stbwd'

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass((91, 34, 45))
b = a.class_var
