# Class Variable is assigned to a variable
class MyClass:
    class_var = [83, 78, 48]

    def __init__(self, instance_var):
        self.instance_var = instance_var


a = MyClass({'hojvs': 69, 'rhfpb': 56, 'npeux': 19})
b = a.class_var
