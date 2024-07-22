# Class Variable is assigned to a variable
class MyClass:
    class_var = [92, 41, 86]

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass({'mcjin': 9, 'lpzpb': 38, 'zuftg': 59})
b = a.class_var
