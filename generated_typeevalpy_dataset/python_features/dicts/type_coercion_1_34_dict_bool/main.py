# Check if tool type coerces integer and string values.


def func1():
    return {'mavuv': 1, 'hjyaa': 15, 'isfdz': 88}


def func2():
    return True


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
