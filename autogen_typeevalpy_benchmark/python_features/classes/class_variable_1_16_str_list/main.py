# Class Variable is assigned to a variable
class MyClass:
    class_var = 'xgqhp'

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass([95, 7, 44])
b = a.class_var
