# A dictionary key is assigned to a function.


def func1():
    return 'ouvyx'


def func2():
    return {'pixnd': 42, 'jycir': 38, 'tiudo': 89}


d = {"a": func1}

d["a"] = func2

e = d["a"]()
