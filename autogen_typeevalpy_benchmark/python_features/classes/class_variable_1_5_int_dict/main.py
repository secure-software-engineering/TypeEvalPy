# Class Variable is assigned to a variable
class MyClass:
    class_var = 96

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass({'xibbw': 57, 'nhpnb': 70, 'vwnfi': 51})
b = a.class_var
