# Class Variable is assigned to a variable
class MyClass:
    class_var = {'caeet': 92, 'tgobw': 14, 'jhtyg': 43}

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(79)
b = a.class_var
