# Program for field sensitivity analysis in depth 3
class A:
    def __init__(self, b):
        self.b = b


class B:
    def __init__(self, c):
        self.c = c


class C:
    def __init__(self, value):
        self.value = value


a = A(B(C(42)))
result = a.b.c.value
