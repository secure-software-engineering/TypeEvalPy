# Class Variable is assigned to a variable
class MyClass:
    class_var = (86, 39, 79)

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass('azpty')
b = a.class_var
