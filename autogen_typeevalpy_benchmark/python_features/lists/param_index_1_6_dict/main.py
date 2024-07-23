# A parameter is used to index a list.


def func2():
    return {'uawzn': 34, 'xdyew': 16, 'bloxd': 61}


def func1(key):
    return ls[key]()


ls = [func1, func2]

a = func1(1)
