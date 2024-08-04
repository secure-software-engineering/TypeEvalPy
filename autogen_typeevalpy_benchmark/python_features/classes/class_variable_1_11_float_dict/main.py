# Class Variable is assigned to a variable
class MyClass:
    class_var = 86.12

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass({'ahrhv': 87, 'ilqva': 54, 'rtdos': 60})
b = a.class_var
