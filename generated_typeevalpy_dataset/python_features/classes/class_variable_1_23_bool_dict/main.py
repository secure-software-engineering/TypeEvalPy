# Class Variable is assigned to a variable
class MyClass:
    class_var = True

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass({'gvbpx': 62, 'juqga': 51, 'wlyus': 23})
b = a.class_var
