# Class Variable is assigned to a variable
class MyClass:
    class_var = {'bxhti': 7, 'fgfod': 44, 'hzjhi': 10}

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(32.36)
b = a.class_var
