# Class Variable is assigned to a variable
class MyClass:
    class_var = {'wimny': 12, 'dfovf': 49, 'ehrwd': 15}

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass('rtkey')
b = a.class_var
