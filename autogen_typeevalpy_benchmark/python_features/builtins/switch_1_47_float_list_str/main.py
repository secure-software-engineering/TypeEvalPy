#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 23.87:
            return [67, 79, 78]
        case [67, 79, 78]:
            return 23.87
        case _:
            return "default"


a = func(23.87)
b = func([67, 79, 78])
c = func('jgvsr')
