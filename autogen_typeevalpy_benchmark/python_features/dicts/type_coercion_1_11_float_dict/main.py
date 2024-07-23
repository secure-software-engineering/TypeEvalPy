# Check if tool type coerces integer and string values.


def func1():
    return 71.84


def func2():
    return {'fvzxn': 45, 'ynbzf': 32, 'hfygq': 14}


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
