# Follow the inheritance chain by calling super.


class A:
    def func(self):
        return 24.02


class B(A):
    def func(self):
        return super().func()


class C(B):
    def func(self):
        return super().func()


c = C()
d = c.func()
