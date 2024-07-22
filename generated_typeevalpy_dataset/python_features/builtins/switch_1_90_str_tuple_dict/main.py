#  A function is defined with switch statement in it.
def func(value):
    match value:
        case 'exegl':
            return (66, 73, 88)
        case (66, 73, 88):
            return 'exegl'
        case _:
            return "default"


a = func('exegl')
b = func((66, 73, 88))
c = func({'kixva': 45, 'speed': 89, 'iadxk': 36})
