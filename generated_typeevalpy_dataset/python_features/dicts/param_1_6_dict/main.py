# A dictionary is passed as a parameter.


def func2():
    return {'pjqsl': 33, 'mhbxt': 79, 'iarob': 86}


def func1(d):
    return d["a"]()


d = {"a": func2}

e = func1(d)
