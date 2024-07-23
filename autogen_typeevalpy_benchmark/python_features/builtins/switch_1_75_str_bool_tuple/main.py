#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'pgepg':
            return False
        case False:
            return 'pgepg'
        case _:
            return "default"


a = func('pgepg')
b = func(False)
c = func((72, 60, 83))
