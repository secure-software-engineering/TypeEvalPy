# Class Variable is assigned to a variable
class MyClass:
    class_var = {'nqpmt': 72, 'msexf': 97, 'mfoqh': 57}

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(True)
b = a.class_var
