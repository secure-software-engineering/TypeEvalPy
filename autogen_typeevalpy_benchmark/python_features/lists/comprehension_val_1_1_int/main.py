# A function is used for the value of a comprehension.


def func(a):
    return a + 31


ls = [func(a) for a in range(10)]
