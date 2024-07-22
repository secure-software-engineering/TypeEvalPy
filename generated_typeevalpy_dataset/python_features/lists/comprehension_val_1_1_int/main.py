# A function is used for the value of a comprehension.


def func(a):
    return a + 70


ls = [func(a) for a in range(10)]
