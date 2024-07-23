# A simple inheritance scheme.


class A:
    def func(self):
        return {'ukfah': 62, 'mvudg': 22, 'rizvj': 55}


class B(A):
    pass


b = B()
c = b.func()
