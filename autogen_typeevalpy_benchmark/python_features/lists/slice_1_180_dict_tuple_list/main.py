# A new list is created as a slice of another one containing functions.


def func1():
    return {'lmpza': 3, 'ejcqa': 78, 'sjcei': 24}


def func2():
    return (58, 29, 17)


def func3():
    return [32, 92, 12]


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
