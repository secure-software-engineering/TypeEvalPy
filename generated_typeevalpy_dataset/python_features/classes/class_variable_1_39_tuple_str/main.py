# Class Variable is assigned to a variable
class MyClass:
    class_var = (48, 12, 27)

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass('jwgru')
b = a.class_var
