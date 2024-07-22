# Class Variable is assigned to a variable
class MyClass:
    class_var = (29, 84, 78)

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass({'chnhj': 86, 'wxhyt': 57, 'hmdbv': 60})
b = a.class_var
