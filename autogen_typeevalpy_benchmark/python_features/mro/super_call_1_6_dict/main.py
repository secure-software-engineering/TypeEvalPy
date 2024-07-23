# Follow the inheritance chain by calling super.


class A:
    def func(self):
        return {'scnwm': 75, 'iychn': 48, 'nwrxn': 59}


class B(A):
    def func(self):
        return super().func()


class C(B):
    def func(self):
        return super().func()


c = C()
d = c.func()
