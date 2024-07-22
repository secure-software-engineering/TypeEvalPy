# Check if tool type coerces integer and string values.


def func1():
    return {'vdgbh': 6, 'lmagb': 85, 'rxlvo': 62}


def func2():
    return 'murwc'


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
