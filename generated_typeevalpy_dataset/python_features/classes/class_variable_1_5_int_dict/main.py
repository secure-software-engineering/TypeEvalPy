# Class Variable is assigned to a variable
class MyClass:
    class_var = 97

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass({'ffydd': 83, 'hmmag': 59, 'aqsfd': 20})
b = a.class_var
