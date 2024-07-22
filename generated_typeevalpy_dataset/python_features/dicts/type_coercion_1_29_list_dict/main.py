# Check if tool type coerces integer and string values.


def func1():
    return [29, 40, 42]


def func2():
    return {'xjide': 4, 'bpupl': 24, 'bgndv': 3}


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
