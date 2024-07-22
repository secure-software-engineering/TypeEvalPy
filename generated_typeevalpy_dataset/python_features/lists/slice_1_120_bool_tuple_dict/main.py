# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return (24, 34, 8)


def func3():
    return {'ohlat': 60, 'ljjrg': 11, 'mudok': 66}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
