# A parameter is used to index a list.


def func2():
    return 43.62


def func1(key):
    return ls[key]()


ls = [func1, func2]

a = func1(1)