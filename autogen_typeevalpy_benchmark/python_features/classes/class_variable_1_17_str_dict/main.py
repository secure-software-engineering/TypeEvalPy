# Class Variable is assigned to a variable
class MyClass:
    class_var = 'qwvse'

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass({'tgead': 58, 'yoodf': 52, 'wcmki': 58})
b = a.class_var
