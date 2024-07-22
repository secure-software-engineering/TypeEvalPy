# A dictionary key is assigned to a function.


def func1():
    return {'yqkoe': 43, 'sposu': 20, 'mivfu': 89}


def func2():
    return (25, 58, 51)


d = {"a": func1}

d["a"] = func2

e = d["a"]()
