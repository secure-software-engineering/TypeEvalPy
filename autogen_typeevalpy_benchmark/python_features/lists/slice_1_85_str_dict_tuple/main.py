# A new list is created as a slice of another one containing functions.


def func1():
    return 'ijpls'


def func2():
    return {'hzfpf': 42, 'xkypj': 48, 'gzkgc': 59}


def func3():
    return (62, 24, 11)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
