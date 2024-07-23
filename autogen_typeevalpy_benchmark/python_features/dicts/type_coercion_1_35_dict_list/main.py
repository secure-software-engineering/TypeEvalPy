# Check if tool type coerces integer and string values.


def func1():
    return {'jpiue': 79, 'vyvqj': 52, 'nxaoh': 79}


def func2():
    return [77, 25, 24]


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
