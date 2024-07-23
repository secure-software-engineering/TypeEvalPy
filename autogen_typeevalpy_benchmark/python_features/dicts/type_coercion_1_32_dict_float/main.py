# Check if tool type coerces integer and string values.


def func1():
    return {'udpoa': 14, 'wiwwb': 8, 'tfcix': 48}


def func2():
    return 65.06


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
