# Check if tool type coerces integer and string values.


def func1():
    return True


def func2():
    return {'jpioi': 62, 'qheel': 97, 'ynvqm': 29}


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
