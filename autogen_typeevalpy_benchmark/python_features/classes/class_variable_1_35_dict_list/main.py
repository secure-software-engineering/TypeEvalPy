# Class Variable is assigned to a variable
class MyClass:
    class_var = {'kczed': 90, 'peohu': 1, 'sezfn': 98}

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass([51, 24, 45])
b = a.class_var
