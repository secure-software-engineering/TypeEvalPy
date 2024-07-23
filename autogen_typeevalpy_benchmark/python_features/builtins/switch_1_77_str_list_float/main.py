#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'uueow':
            return [67, 3, 83]
        case [67, 3, 83]:
            return 'uueow'
        case _:
            return "default"


a = func('uueow')
b = func([67, 3, 83])
c = func(70.41)
