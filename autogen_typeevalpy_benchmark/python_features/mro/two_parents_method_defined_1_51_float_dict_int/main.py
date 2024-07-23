# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return 26.01


class B:
    def func(self):
        return {'agvvu': 26, 'gsepu': 65, 'sbnbk': 77}


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return 83


c = C()
d = c.func()
