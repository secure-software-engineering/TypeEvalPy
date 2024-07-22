# Class Variable is assigned to a variable
class MyClass:
    class_var = 'tamna'

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(62)
b = a.class_var
