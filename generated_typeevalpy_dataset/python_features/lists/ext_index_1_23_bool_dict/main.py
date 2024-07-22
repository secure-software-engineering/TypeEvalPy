# A key is imported from an external source and used to index a list.


from ext import key


def func1():
    return True


def func2():
    return {'kmnkc': 100, 'ludmy': 25, 'yafgd': 41}


ls = [func1, func2]

a = ls[key]()
