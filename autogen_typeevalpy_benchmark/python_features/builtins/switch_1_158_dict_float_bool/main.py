#  A function is defined with switch statement in it.
def func(value):
    match value:
        case {'gwqol': 73, 'mwopx': 9, 'nxvmf': 17}:
            return 60.7
        case 60.7:
            return {'gwqol': 73, 'mwopx': 9, 'nxvmf': 17}
        case _:
            return "default"


a = func({'gwqol': 73, 'mwopx': 9, 'nxvmf': 17})
b = func(60.7)
c = func(True)
