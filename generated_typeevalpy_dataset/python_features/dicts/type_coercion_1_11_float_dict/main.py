# Check if tool type coerces integer and string values.


def func1():
    return 83.03


def func2():
    return {'irgnf': 61, 'habce': 98, 'dqmmb': 49}


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
