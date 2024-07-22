# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return {'alctk': 82, 'dupop': 6, 'grnrk': 34}


def func2():
    return False


ls = [func1, func2]

a = ls[key]()
