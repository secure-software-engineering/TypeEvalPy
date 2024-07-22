# A nested comprehension.


def func1(a):
    return a + 69


def func2(a):
    return a + 69


c = [func1(a) for a in [func2(b) for b in range(10)]]
