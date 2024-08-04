# Class Variable is assigned to a variable
class MyClass:
    class_var = {'gpwcn': 1, 'hjboe': 7, 'onxgg': 30}

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass((45, 52, 29))
b = a.class_var
