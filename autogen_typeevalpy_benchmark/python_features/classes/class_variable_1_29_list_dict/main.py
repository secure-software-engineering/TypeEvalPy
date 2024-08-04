# Class Variable is assigned to a variable
class MyClass:
    class_var = [18, 93, 54]

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass({'ryobc': 10, 'nytcc': 41, 'tmggw': 59})
b = a.class_var
