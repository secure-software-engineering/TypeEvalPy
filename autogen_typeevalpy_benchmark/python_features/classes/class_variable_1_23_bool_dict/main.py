# Class Variable is assigned to a variable
class MyClass:
    class_var = True

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass({'gvfal': 9, 'ncwet': 25, 'myjiw': 52})
b = a.class_var
