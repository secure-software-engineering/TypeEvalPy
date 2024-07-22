# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return {'ccawr': 24, 'ymjat': 50, 'nobme': 68}


def func2():
    return [16, 74, 67]


ls = [func1, func2]

a = ls[key]()
