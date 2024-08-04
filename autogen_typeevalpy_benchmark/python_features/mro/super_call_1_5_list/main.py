# Follow the inheritance chain by calling super.


class A:
    def func(self):
        return [27, 65, 87]


class B(A):
    def func(self):
        return super().func()


class C(B):
    def func(self):
        return super().func()


c = C()
d = c.func()
