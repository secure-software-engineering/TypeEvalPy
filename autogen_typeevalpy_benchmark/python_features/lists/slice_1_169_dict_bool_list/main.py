# A new list is created as a slice of another one containing functions.


def func1():
    return {'hdhxa': 79, 'eyzni': 31, 'zfmha': 19}


def func2():
    return True


def func3():
    return [3, 68, 41]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
