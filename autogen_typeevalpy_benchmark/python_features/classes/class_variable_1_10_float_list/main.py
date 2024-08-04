# Class Variable is assigned to a variable
class MyClass:
    class_var = 20.44

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass([46, 77, 39])
b = a.class_var
