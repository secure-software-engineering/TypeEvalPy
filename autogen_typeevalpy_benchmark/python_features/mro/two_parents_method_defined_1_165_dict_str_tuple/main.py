# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return {'klpbt': 83, 'pwiic': 42, 'ulsui': 98}


class B:
    def func(self):
        return 'dqhgd'


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return (72, 34, 51)


c = C()
d = c.func()
