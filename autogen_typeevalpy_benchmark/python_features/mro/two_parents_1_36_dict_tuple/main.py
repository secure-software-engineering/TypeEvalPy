# A class is defined with two parents. The correct ordering must be preserved when calling a parent function.


class A:
    def func(self):
        return {'pccjg': 14, 'bgbqt': 38, 'xcgel': 16}


class B:
    def __init__(self):
        pass

    def func(self):
        return (50, 55, 20)


class C(A, B):
    pass


c = C()
d = c.func()
