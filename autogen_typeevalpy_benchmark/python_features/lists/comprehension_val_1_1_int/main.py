# A function is used for the value of a comprehension.


def func(a):
    return a + 55


ls = [func(a) for a in range(10)]
