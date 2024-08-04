# Check if tool type coerces integer and string values.


def func1():
    return {'kuycp': 81, 'bjlgr': 42, 'doiqa': 1}


def func2():
    return (81, 3, 46)


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
