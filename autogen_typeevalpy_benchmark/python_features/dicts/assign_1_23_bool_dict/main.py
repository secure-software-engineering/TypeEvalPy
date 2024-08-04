# A dictionary key is assigned to a function.


def func1():
    return False


def func2():
    return {'dlwcx': 9, 'cofya': 29, 'xbpvt': 51}


d = {"a": func1}

d["a"] = func2

e = d["a"]()
