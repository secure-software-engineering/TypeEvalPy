# A new list is created as a slice of another one containing functions.


def func1():
    return 56.97


def func2():
    return (42, 94, 96)


def func3():
    return {'qcjic': 79, 'xamqw': 66, 'rddak': 100}


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
