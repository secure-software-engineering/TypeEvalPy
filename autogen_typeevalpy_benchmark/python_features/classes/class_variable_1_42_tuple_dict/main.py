# Class Variable is assigned to a variable
class MyClass:
    class_var = (92, 20, 78)

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass({'dckhf': 14, 'yklyq': 76, 'vislp': 6})
b = a.class_var
