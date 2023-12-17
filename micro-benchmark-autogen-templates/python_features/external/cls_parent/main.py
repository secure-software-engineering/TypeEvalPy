# A `self` call to a function defined inside an external parent.
from typeevalpy_external_module.ext import Parent


class A(Parent):
    def fn(self):
        return self.parent_fun()


a = A()
b = a.fn()
