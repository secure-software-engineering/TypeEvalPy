#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [34, 88, 74]:
            return True
        case True:
            return [34, 88, 74]
        case _:
            return "default"


a = func([34, 88, 74])
b = func(True)
c = func({'ceffw': 18, 'vnvxd': 85, 'oalvf': 90})
