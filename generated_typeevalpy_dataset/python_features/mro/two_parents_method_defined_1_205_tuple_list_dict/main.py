# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (45, 100, 51)


class B:
    def func(self):
        return [88, 7, 26]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'ynsms': 73, 'sdnlg': 70, 'mrnve': 26}


c = C()
d = c.func()
