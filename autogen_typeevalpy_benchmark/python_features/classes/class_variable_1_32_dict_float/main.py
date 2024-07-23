# Class Variable is assigned to a variable
class MyClass:
    class_var = {'blgbx': 93, 'liuev': 51, 'wzwfx': 24}

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass(70.0)
b = a.class_var
