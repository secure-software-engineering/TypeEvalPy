# A class is instantiated and then its function is called directly after the instantiation.


class MyClass:
    def __init__(self):
        pass

    def func(self):
        return [53, 66, 93]


a = MyClass().func()
