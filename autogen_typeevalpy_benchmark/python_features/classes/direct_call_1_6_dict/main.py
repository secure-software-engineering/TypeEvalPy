# A class is instantiated and then its function is called directly after the instantiation.


class MyClass:
    def __init__(self):
        pass

    def func(self):
        return {'kcfao': 78, 'kcekx': 7, 'naysk': 66}


a = MyClass().func()
