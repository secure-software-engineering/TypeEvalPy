# A dictionary key is assigned to a function.


def func1():
    return (8, 35, 96)


def func2():
    return {'yytre': 83, 'wodqv': 47, 'ucpry': 85}


d = {"a": func1}

d["a"] = func2

e = d["a"]()
