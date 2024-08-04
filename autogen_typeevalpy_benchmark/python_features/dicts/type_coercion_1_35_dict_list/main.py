# Check if tool type coerces integer and string values.


def func1():
    return {'dtvxk': 24, 'kggcl': 99, 'wgxmi': 17}


def func2():
    return [39, 52, 79]


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
