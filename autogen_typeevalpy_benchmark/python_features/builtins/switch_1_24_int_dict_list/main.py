#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 4:
            return {'gjnam': 18, 'wjvgq': 76, 'uuvnq': 98}
        case {'gjnam': 18, 'wjvgq': 76, 'uuvnq': 98}:
            return 4
        case _:
            return "default"


a = func(4)
b = func({'gjnam': 18, 'wjvgq': 76, 'uuvnq': 98})
c = func([67, 47, 9])
