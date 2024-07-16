# Call a function with keyword arguments.


def concatenate(**kwargs):
    result = <value1>
    for arg in kwargs.values():
        result += arg
    return result


c = concatenate(a=<value1>, b=<value1>, c=<value1>)
