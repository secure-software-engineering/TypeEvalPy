# Class Variable is assigned to a variable
class MyClass:
    class_var = {'vamre': 37, 'hxler': 88, 'ueyty': 79}

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass('qjqts')
b = a.class_var
