# A method returns a method of its parent class.


class A:
    def func1(self):
        return [3, 83, 6]


class B(A):
    def func2(self):
        return self.func1


b = B()
fn = b.func2()
c = fn()
