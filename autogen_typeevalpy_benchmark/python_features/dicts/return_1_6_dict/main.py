# A dictionary is returned.


def func2():
    return {'ybyhu': 51, 'jjsfa': 63, 'judwg': 18}


def func1():
    d = {"a": func2}
    return d


b = func1()
c = b["a"]()
