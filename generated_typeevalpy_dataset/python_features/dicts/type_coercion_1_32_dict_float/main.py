# Check if tool type coerces integer and string values.


def func1():
    return {'kzdnh': 35, 'nuvnq': 38, 'dxdkq': 51}


def func2():
    return 90.69


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
