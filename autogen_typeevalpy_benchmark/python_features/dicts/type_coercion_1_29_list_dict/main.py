# Check if tool type coerces integer and string values.


def func1():
    return [45, 83, 99]


def func2():
    return {'cpjrt': 78, 'dbhxd': 91, 'sksjz': 45}


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
