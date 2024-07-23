#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 7:
            return [17, 12, 80]
        case [17, 12, 80]:
            return 7
        case _:
            return "default"


a = func(7)
b = func([17, 12, 80])
c = func({'rkrsw': 37, 'zlgpc': 45, 'hvssv': 74})
