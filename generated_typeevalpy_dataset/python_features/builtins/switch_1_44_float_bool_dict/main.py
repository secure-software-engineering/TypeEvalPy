#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 66.8:
            return False
        case False:
            return 66.8
        case _:
            return "default"


a = func(66.8)
b = func(False)
c = func({'idrgk': 29, 'kktsu': 88, 'emgha': 80})
