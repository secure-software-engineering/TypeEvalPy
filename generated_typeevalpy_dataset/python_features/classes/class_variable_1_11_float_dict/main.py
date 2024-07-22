# Class Variable is assigned to a variable
class MyClass:
    class_var = 13.98

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass({'acxad': 86, 'imlxj': 50, 'lymqu': 97})
b = a.class_var
