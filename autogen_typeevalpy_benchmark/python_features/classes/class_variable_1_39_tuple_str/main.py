# Class Variable is assigned to a variable
class MyClass:
    class_var = (27, 84, 40)

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass('ivauc')
b = a.class_var
