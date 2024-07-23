# Check if tool type coerces integer and string values.


def func1():
    return {'nqiqh': 22, 'lpntw': 67, 'caqem': 56}


def func2():
    return 'tdtbr'


d = {1: func1, "1": func2}

e = d[1]()
f = d["1"]()
