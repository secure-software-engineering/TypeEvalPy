# A class is defined inheriting from two parents. However all the functions called are defined in the class itself.


class A:
    def __init__(self):
        pass

    def func(self):
        return (36, 25, 10)


class B:
    def func(self):
        return [11, 69, 2]


class C(A, B):
    def __init__(self):
        pass

    def func(self):
        return {'fquvd': 39, 'suobj': 18, 'uwtze': 53}


c = C()
d = c.func()
