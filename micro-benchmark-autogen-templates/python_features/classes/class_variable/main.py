# Class Variable is assigned to a variable
class MyClass:
    class_var = <value1>

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(<value2>)
b = a.class_var
