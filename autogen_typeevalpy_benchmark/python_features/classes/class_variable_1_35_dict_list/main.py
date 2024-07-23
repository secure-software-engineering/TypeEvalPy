# Class Variable is assigned to a variable
class MyClass:
    class_var = {'xyibh': 47, 'bfaba': 25, 'fyick': 96}

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass([70, 68, 92])
b = a.class_var
